###############################################################################
#                Simple Animator | Template v 1.0 | UPBGE 0.2.3               #
###############################################################################
#                      Created by: Guilherme Teres Nunes                      #
#                       Access: youtube.com/UnidayStudio                      #
#                               github.com/UnidayStudio                       #
###############################################################################
# Simple Animator Component:
#	Attach this component to the armature of your character. It's important
# that the armature is parented with an capsule object with physics type equals
# to Character.
#	This component will automatically align the armature to the move direction
# of your character, runs the right animations accordding to the speed and if
# the character is on air or not.
###############################################################################
import bge
from mathutils import Vector
from math import pi
from collections import OrderedDict

def clamp(x, a, b):
	return min(max(a, x), b)

class SimpleAnimator(bge.types.KX_PythonComponent):
	args = OrderedDict([
		("Activate"              , True),
		("Max Walk Speed"        , 0.1),
		("Max Run Speed"         , 0.2),
		("Suspend Child Physics" , True),
		("Align To Move Direction", True),
		("Align Smooth"          , 0.5),

		("Idle Animation"        , ""),
		("Idle Frame Start-End"  , Vector([0,10])),

		("Walk Animation"        , ""),
		("Walk Frame Start-End"  , Vector([0, 10])),

		("Run Animation"         , ""),
		("Run Frame Start-End"   , Vector([0, 10])),

		("Jump Up Animation"     , ""),
		("Jump Up Frame Start-End", Vector([0, 10])),

		("Jump Down Animation"   , ""),
		("Jump Down Frame Start-End", Vector([0, 10])),
	])

	# Start Function
	def start(self, args):
		self.active = args["Activate"]

		self.__lastPosition  = self.object.worldPosition.copy()
		self.__moveDirection = None
		self.__alignMoveDir  = args["Align To Move Direction"]
		self.alignSmooth     = 1 - clamp( args["Align Smooth"], 0, 1)

		self.__animIdle = [args["Idle Animation"], args["Idle Frame Start-End"]]
		self.__animWalk = [args["Walk Animation"], args["Walk Frame Start-End"]]
		self.__animRun  = [args["Run Animation"], args["Run Frame Start-End"]]
		self.__animJumpUp  = [args["Jump Up Animation"], args["Jump Up Frame Start-End"]]
		self.__animJumpDown= [args["Jump Down Animation"], args["Jump Down Frame Start-End"]]

		self.maxWalkSpeed = args["Max Walk Speed"]
		self.maxRunSpeed  = args["Max Run Speed"]

		# Suspend physics:
		if args["Suspend Child Physics"]:
			self.object.suspendPhysics()
			for child in self.object.children:
				child.suspendPhysics()

		self.character = bge.constraints.getCharacter(self.object.parent)
		# Error:
		if self.character == None:
			print("[Animator] Error: Can't get the Character constraint from the armature parent.")

	# Updates the move direction
	def __updateMoveDirection(self):
		self.__moveDirection = self.object.worldPosition - self.__lastPosition
		self.__lastPosition = self.object.worldPosition.copy()

	# Runs an animation
	def __animate(self, animData, blend=4):
		self.object.playAction(animData[0], animData[1][0], animData[1][1], blendin=blend)

	# Handles animations on ground (Walk, Run, Idle).
	def __handleGroundAnimations(self):
		# TO DO: Interpolate between these animations according to the speed.
		speed = self.__moveDirection.length
		if speed == 0:#<= 0.001:
			self.__animate(self.__animIdle)
		elif speed <= self.maxWalkSpeed+0.001:
			self.__animate(self.__animWalk)
		else:
			self.__animate(self.__animRun)

	# Handles animations on air (Jump).
	def __handleAirAnimations(self):
		if self.__moveDirection[2] > 0:
			self.__animate(self.__animJumpUp)
		else:
			self.__animate(self.__animJumpDown, 10)

	# Returns the current move direction
	def getMoveDirection(self):
		return self.__moveDirection

	# Align the armature to the move direction
	def alignToMoveDirection(self):
		length = self.__moveDirection.length
		if length >= 0.01:
			# First checks if the move direction is the opposite of the current
			# direction. If so, applies a small rotation just to avoid a weird
			# delay that alignAxisToVect has in this case.
			vec = self.object.worldOrientation * Vector([0,1,0])
			if vec.angle(self.__moveDirection) >= pi-0.01:
				self.object.applyRotation([0,0,0.01], False)

			length = clamp(length*20, 0, 1) * self.alignSmooth
			self.object.alignAxisToVect(self.__moveDirection, 1, length)
			self.object.alignAxisToVect([0,0,1], 2, 1)

	# Update Function
	def update(self):
		self.__updateMoveDirection()

		if self.active:
			if self.__alignMoveDir:
				self.alignToMoveDirection()

			if self.character.onGround:
				self.__handleGroundAnimations()
			else:
				self.__handleAirAnimations()