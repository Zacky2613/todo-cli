# todo-cli

A python application tool to handle your tasks straight from the command line.

## Features/Usage

There are 3 categories which are todo, doing, and done. The following commands are how to interact with them

<details> 
    <summary> Add Task </summary>
    Add a task to one of the categories

    Example: `[*] Task: todo update README.md file`

</details>


<details> 
    <summary> Move Task </summary>
    Move a task from one category to another by task id (the 0)

    Example: `[*] Task: todo 0 doing`

</details>


<details> 
    <summary> Clear category </summary>
    Clear a category in its entirety.

    Example: `[*] Category: todo`
</details> 

<details> 
    <summary> Clear all </summary>
    Just the input and it clears all

</details>

## Inspiration

This is inspired off of <a href="https://github.com/kennxdy/doddot">kennxdy's doddot project.</a>

How the categories and input selection are displayed is pretty close to kennxdy's. However, I've rewritten all the code and move the code structure around while having a completely different way of handling data in the backend.

