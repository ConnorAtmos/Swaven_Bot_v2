[Back to DOCS.md](DOCS.md)

Import Statement: `from toolbox import discord_functions`

Alternative Import Statement: `from toolbox.discord_functions import *`

# >  function get_role_names_from_string #

### [def get_role_names_from_string(ctx, role_str: str):](./../toolbox/discord_functions.py#L3) 

Note

```python
    This function will remove duplicates as well
```

Param

```python
    role_str: str
        A string of roles separated by commas (i.e. "role1, role2, role3")
        Also can be separated by spaces (i.e. "role1 role2 role3")
        This can be either the role name or the role id/mention
```

Return

```python
    roles: list
        A list of role names
```

Example

```python
    # This is an example of how to use this function, within a command
    role_str = "role1, role2, role3"
    roles = get_role_names_from_string(ctx, role_str)
    ctx.respond(f"Roles {roles} located.")
```

# >  function get_role_id #

### [def get_role_id(ctx, role_name):](./../toolbox/discord_functions.py#L47) 

Note

```python
    This function will raise an error if the role does not exist
```

Param

```python
    ctx: discord_slash.context.SlashContext
        The context of the command
    role_name: str
        The name of the role
```

Return

```python
    role_id: int
        The id of the role
```

Example

```python
    # This is an example of how to use this function, within a command
    role_name = "role1"
    role_id = get_role_id(ctx, role_name)
    ctx.respond(f"Role {role_name} has id {role_id}")
```

# >  function remove_emoji_numbers #

### [def remove_emoji_numbers(text: str):](./../toolbox/discord_functions.py#L82) 

Note

```python
    This function removes numbers from discord emojis for tts. (i.e. <:emoji:123456789> to emoji)
```

Param

```python
    text: str
        The text to remove numbers from
```

Return

```python
    text: str
        The text with numbers removed
```

Example

```python
    text = remove_emoji_numbers(text)
```

# >  function convert_ping_to_username #

### [def convert_ping_to_username(text, guild):](./../toolbox/discord_functions.py#L113) 

# >  function get_emoji_from_id #

### [def get_emoji_from_id(ctx, id) -> str:](./../toolbox/discord_functions.py#L125) 

Param

```python
    ctx: discord_slash.context.SlashContext
        The context of the command
    id: int
        The id of the emoji
```

Return

```python
    emoji: str
        The emoji
```

