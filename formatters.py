from typing import Union
import datetime, discord, time

# basic markdown
def bold(content: str) -> str:
    """Returns bold string => **content**"""
    return f"**{content}**"
def italic(content: str) -> str:
    """Returns italic string => _content_"""
    return f"_{content}_"
def strikethrough(content: str) -> str:
    """Returns strikethrough string => ~~content~~"""
    return f"~~{content}~~"
def underline(content: str) -> str:
    """Returns underlined string => __content__"""
    return f"__{content}__"
def spoiler(content: str) -> str:
    """Returns spoilered (hidden) string => ||content||"""
    return f"||{content}||"
def quote(content: str) -> str:
    """Returns quoted string => > content"""
    return f"> {content}"
def block_quote(content: str) -> str:
    """Returns block quoted (multi-line quote) 
    string => >>> content"""
    return f">>> {content}"

# links
def hide_link_embed(url: str) -> str:
    """Returns URL with no embeds => <content>"""
    return f"<{url}>"
def hyperlink(url: str,content,title=None) -> str:
    """Returns a hyperlink string => [content](url \"title\") 
    or [content](url)"""
    return (
        f'[{content}]({url} "{title}")' if (title) else f"[{content}]({url})"
    )

# code blocks
def inline_code(content: str) -> str:
    """Returns string wrapped in single backticks => `content`"""
    return f"`{content}`"
def code_block(content: str,language: str="") -> str:
    """Returns string wrapped in triple backticks => ```language\ncontent\n```"""
    return f"```{language}\n{content}\n```"

# timestamps
def time_format(time: Union[int, datetime.datetime],relative: str=None) -> str:
    """Takes a datetime.datetime object or a UNIX timestamp, and returns a Discord timestamp markdown => <t:timestamp> or <t:timestamp:relative>"""
    relatives = ["D","d","f","F","T","t","R"]
    relative_formatter = lambda x,y=None: f"<t:{x}{'' if (not y) else f':{y}'}>"

    if (not (relative in relatives)) and (relative):
        raise ValueError(f'bad format style "{relative}": must be {", ".join(relatives)}')

    if (isinstance(time,int)):
        ts = time
    if(isinstance(time,datetime.datetime)):
        ts = round(int(time.timestamp()))
    return relative_formatter(ts,relative)

# emojis
def emoji_format(emoji_id: int,animated: bool=False) -> str:
    """Takes an emoji ID and returns a fully qualified emoji identifier =>\
    <a:_:emoji_id> or <:_:emoji_id>"""
    return f"<{'a' if (animated) else ''}:_:{emoji_id}>"

# mentions
def user_mention(id: discord.User):
    """Returns a user mention string => <@id>"""
    return f"<@{id}>"
def member_nickname_mention(id: discord.Member):
    """Returns a member nickname mention string => <@!id>"""
    return f"<@!{id}>"
def channel_mention(id: discord.abc.GuildChannel):
    """Returns a channel mention string => <#id>"""
    return f"<#{id}>"
def role_mention(id: discord.Role):
    """Returns a role mention string => <@&id>"""
    return f"<@&{id}>"
