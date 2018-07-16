# **Character Controller** Template | Third/First Person and much more!
###### For UPBGE 0.2.3
This templates was created to help Blender Game Engine (UPBGE) users to create games or any kind of interactive things that requests a Character Controller. Easy to use, easy to attach to your project.

To use, just download the files, open it on UPBGE (version 0.2.3 recommended) and you're done!
You can use this template in your projects, even for commercial projects. Just credit me for this.:)
It's very easy to use in your projects: Just load this script into your .blend file (or paste them in the same folder that your .blend is), select the object that you want, and attach the script into the object's components.

## Character Controller Component
This component will serve as a **Character Controller** for your game. With this, you can easly made an object move using W,A,S,D, run with LSHIFT and Jump with SPACE.

Create a capsule for your character, set the physics type to "Character" and attach this Component to them.

It's very simple to configure:
- **Activate**: If you want this component running.
- **Walk Speed**: The character's walk speed.
- **Run Speed**: The character's run speed.
- **Max Jumps**: The character's max jumps. Set to zero (0) if you don't want the character to jump.
- **Static Jump Direction**:  If you want to make your character jump in a static direction, activate "Static Jump Direction". It means that, if the player wasn't moving when he pressed Space, the character will jump up and the player will not be able to change this during the jump. The same for when he was moving when pressed Space. The jump direction will be the character direction when the player press space.
- **Avoid Sliding**: If your character object have Collision Bounds activated, I'd recommend to enable the "Avoid Sliding" option. If so, the component will avoid the character from sliding on ramps.
- **Make Object Invisible**: Makes the object invisible ingame (useful if you attach this component to a capsule object that have a armature inside).

## First Person Camera Component
This component was created to be attached to your camera to give you a great mouselook control. Very useful for First Person games.

To use, add a camera in your scene, parent them into your character capsule (you can use the Character controller Component on it), and attach this Component to the camera. Don't forgot to position the camera in a place near the "head" of your character.

You can configure the mouse sensibility, invert X or Y axis and enable/disable the camera rotation limit.
It's very simple to configure:
- **Activate**: If you want this component running.
- **Mouse Sensibility**: The mouse sensibility.
- **Invert Mouse X Axis**: To invert the mouselook on the X axis.
- **Invert Mouse Y Axis**: To invert the mouselook on the Y axis.
- **Limit Camera Rotation**: Limits the camera rotation on the X local axis. Very useful for First Person games to avoid the camera from flip upside down.

## Third Person Camera Component
TO DO.
It's very simple to configure:
- **To Do**: WIP.

Created by **Guilherme Teres Nunes**

Access my youtube channel:
## [Uniday Studio on Youtube](youtube.com/UnidayStudio)