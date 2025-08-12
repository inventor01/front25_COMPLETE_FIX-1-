#!/usr/bin/env python3
"""
Simple Discord bot token test
"""

import os
import discord
import asyncio
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_discord_connection():
    """Test Discord bot connection and basic functionality"""
    
    # Get token from environment
    token = os.getenv('DISCORD_TOKEN')
    
    if not token:
        logger.error("❌ No DISCORD_TOKEN found in environment")
        return False
        
    logger.info(f"🔑 Testing Discord token: {token[:20]}... ({len(token)} chars)")
    
    # Create bot instance with minimal intents
    intents = discord.Intents.default()
    intents.message_content = True
    
    bot = discord.Client(intents=intents)
    
    @bot.event
    async def on_ready():
        logger.info(f"✅ Discord bot connected successfully!")
        logger.info(f"👤 Bot user: {bot.user.name} (ID: {bot.user.id})")
        logger.info(f"🔗 Guild count: {len(bot.guilds)}")
        
        # Test completed - disconnect
        await bot.close()
    
    @bot.event
    async def on_connect():
        logger.info("🔗 Discord WebSocket connected")
    
    @bot.event  
    async def on_disconnect():
        logger.info("🔌 Discord WebSocket disconnected")
        
    try:
        # Test connection with timeout
        await asyncio.wait_for(bot.start(token), timeout=30.0)
        return True
        
    except discord.LoginFailure as e:
        logger.error(f"❌ Discord login failed: {e}")
        logger.error("💡 Check if token is valid and has proper bot permissions")
        return False
        
    except asyncio.TimeoutError:
        logger.error("❌ Discord connection timeout")
        return False
        
    except Exception as e:
        logger.error(f"❌ Discord connection error: {e}")
        return False

if __name__ == "__main__":
    try:
        success = asyncio.run(test_discord_connection())
        if success:
            logger.info("✅ Discord token test completed successfully")
        else:
            logger.error("❌ Discord token test failed")
    except Exception as e:
        logger.error(f"❌ Test script error: {e}")