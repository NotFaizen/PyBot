import discord

__all__ = ("Color","Colour")
class Color(discord.colour.Colour):
  @classmethod
  def medium_azure(cls):
    return cls(0x4b92db)
  @classmethod
  def azure(cls):
    return cls(0x007fff)
  @classmethod
  def pale_azure(cls):
    return cls(0xf0ffff)
  @classmethod
  def royal_azure(cls):
    return cls(0x003fff)
  @classmethod
  def indianred(cls):
    return cls(0xBB4369)
Colour = Color


