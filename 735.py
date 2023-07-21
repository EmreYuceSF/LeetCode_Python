def asteroidCollision(asteroids: list[int]):
    """
    Simulates the collision of asteroids moving in different directions and returns a list of asteroids
    after the collisions have been resolved.

    Parameters:
        asteroids (list[int]): A list of integers representing the directions of asteroids. Positive
                               integers indicate asteroids moving to the right, and negative integers
                               indicate asteroids moving to the left.

    Returns:
        list[int]: A list of integers representing the directions of asteroids after the collisions
                   have been resolved.

    Algorithm:
        1. Initialize an empty stack to store the asteroids while handling collisions.
        2. Iterate through each asteroid in the input 'asteroids' list.
        3. While there are asteroids in the stack and the current asteroid is moving left (negative value),
           and the top of the stack is moving right (positive value), check for collisions.
        4. If the absolute value of the current asteroid is greater than the top of the stack, it means the current
           asteroid destroys the top one. In this case, remove the top asteroid from the stack and add the current
           asteroid to the stack.
        5. If the absolute value of the current asteroid is equal to the top of the stack, both asteroids destroy each
           other, so remove the top asteroid from the stack and move to the next asteroid.
        6. If neither of the above conditions is met, break the loop as there are no collisions, and add the current
           asteroid to the stack.
        7. The loop's 'else' block is executed only if no 'break' statement was encountered in the loop.
           It executes when all the collisions for the current asteroid have been handled, and it's safe to add it to
           the stack without destroying any other asteroid.
        8. Return the stack, which contains the list of asteroids after the collisions have been resolved.
    """

    stack = []

    for asteroid in asteroids:
        while stack and asteroid < 0 < stack[-1]:
            # Check for collisions when current asteroid is moving left (negative) and the top of the stack is moving right (positive).
            if abs(asteroid) > stack[-1]:
                # Current asteroid destroys the top one, remove the top asteroid from the stack and add the current one.
                stack.pop()
                stack.append(asteroid)
            elif abs(asteroid) == stack[-1]:
                # Both asteroids have the same size, so they destroy each other, remove the top asteroid from the stack.
                stack.pop()
                break
            else:
                # No collision occurs, break the loop as there are no more collisions to handle.
                break
        else:
            # The 'else' block is executed when all the collisions for the current asteroid have been handled.
            # It's safe to add the current asteroid to the stack without destroying any other asteroid.
            stack.append(asteroid)

    return stack


print(asteroidCollision([8, 5, -5]))  # Output: [8]
