from pyrogram.errors.exceptions.bad_request_400 import StickerEmojiInvalid 
import requests
import m3u8
import json
import subprocess
from pyrogram import Client, filters
from pyrogram.types.messages_and_media import message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import FloodWait
from pyromod import listen
from pyrogram.types import Message    
from p_bar import progress_bar    
from subprocess import getstatusoutput    
from aiohttp import ClientSession    
import helper    
from logger import logging    
import time    
import asyncio    
from pyrogram.types import User, Message    
import sys    
import re    
import os 
import urllib
import urllib.parse
import tgcrypto
import cloudscraper
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from base64 import b64encode, b64decode
from helper import *
from config import API_ID, API_HASH, BOT_TOKEN

# watermark_text = ""

bot = Client("bot",                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
             bot_token=BOT_TOKEN,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
             api_id= API_ID,                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
             api_hash=API_HASH)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

owner_id = [6877021488]
auth_users = [6877021488]
photo1 = 'https://envs.sh/PQ_.jpg'
getstatusoutput(f"wget {photo1} -O 'photo.jpg'")    
photo = "photo.jpg"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              
 
api_url = "http://master-api-v3.vercel.app/"
api_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzkxOTMzNDE5NSIsInRnX3VzZXJuYW1lIjoi4p61IFtvZmZsaW5lXSIsImlhdCI6MTczODY5MjA3N30.SXzZ1MZcvMp5sGESj0hBKSghhxJ3k1GTWoBUbivUe1I"
token_cp ='eyJjb3Vyc2VJZCI6IjQ1NjY4NyIsInR1dG9ySWQiOm51bGwsIm9yZ2lkIjo0ODA2MTksImNhdGVnb3J5SWQiOm51bGx9r'

# Store user tokens temporarily
user_tokens = {}
current_extracted_file = {}

@bot.on_message(filters.command("start"))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
async def account_login(bot: Client, m: Message):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    await m.reply_text('''🎉 <b>Welcome to DRM Bot! </b>🎉
    
<b>You can have access to download all Non-DRM+Decrypted DRM Bot 🔐 including:</b>
<blockquote><i>
   • 📚 Appx Zip
   • 🎓 Classplus DRM+ NDRM
   • 🧑‍🏫 PhysicsWallah DRM
   • 📚 CareerWill + PDF
   • 🎓 Khan GS
   • 🎓 Study Iq DRM
   • 🚀 APPX + APPX DEC PDF
   • 🎓 Vimeo Protection
   • 🎓 Brightcove Protection
   • 🎓 Visionias Protection
   • 🎓 Zoom Video
   • 🎓 All Non DRM+DEC DRM
   • 🎓 MPD URLs if the key is known (e.g., Mpd_url?key=key XX:XX)
</blockquote></i>
<b>🚀 You are not subscribed to any plan yet!</b>

<blockquote><i>💵 Monthly Plan: ₹ 400</blockquote></i>
<b>If you want to buy membership of the bot, feel free to contact the Bot</b> [🅱🅴🅰🆂🆃👑](https://t.me/chiru52)''')
# File paths
SUBSCRIPTION_FILE = "subscription_data.txt"

# Admin ID
YOUR_ADMIN_ID = 6877021488

# Function to read subscription data
def read_subscription_data():
    if not os.path.exists(SUBSCRIPTION_FILE):
        return []
    with open(SUBSCRIPTION_FILE, "r") as f:
        return [line.strip().split(",") for line in f.readlines()]

# Function to write subscription data
def write_subscription_data(data):
    with open(SUBSCRIPTION_FILE, "w") as f:
        for user in data:
            f.write(",".join(user) + "\n")

# Admin-only decorator
def admin_only(func):
    async def wrapper(client, message: Message):
        if message.from_user.id != YOUR_ADMIN_ID:
            await message.reply_text("You are not authorized to use this command.")
            return
        await func(client, message)
    return wrapper

# /id Command - Show Group/Channel ID
@bot.on_message(filters.command(["id"]))
async def id_command(client, message: Message):
    chat_id = message.chat.id
    await message.reply_text(
        f"🎉 **Success!**\n\n"
        f"🆔 **This Group/Channel ID:**\n`{chat_id}`\n\n"
        f"📌 **Use this ID for further requests.**\n\n"
        f"🔗 To link this group/channel, use the following command:\n"
        f"👉 `/add_channel {chat_id}`"
    )


# 1. /adduser
@bot.on_message(filters.command("adduser") & filters.private)
@admin_only
async def add_user(client, message: Message):
    try:
        _, user_id, expiration_date = message.text.split()
        subscription_data = read_subscription_data()
        subscription_data.append([user_id, expiration_date])
        write_subscription_data(subscription_data)
        await message.reply_text(f"User {user_id} added with expiration date {expiration_date}.")
    except ValueError:
        await message.reply_text("Invalid command format. Use: /adduser <user_id> <expiration_date>")


# 2. /removeuser
@bot.on_message(filters.command("removeuser") & filters.private)
@admin_only
async def remove_user(client, message: Message):
    try:
        _, user_id = message.text.split()
        subscription_data = read_subscription_data()
        subscription_data = [user for user in subscription_data if user[0] != user_id]
        write_subscription_data(subscription_data)
        await message.reply_text(f"User {user_id} removed.")
    except ValueError:
        await message.reply_text("Invalid command format. Use: /removeuser <user_id>")

YOUR_ADMIN_ID = 6877021488

# Helper function to check admin privilege
def is_admin(user_id):
    return user_id == YOUR_ADMIN_ID

# Command to show all users (Admin only)
@bot.on_message(filters.command("users") & filters.private)
async def show_users(client, message: Message):
    user_id = message.from_user.id

    if not is_admin(user_id):
        await message.reply_text("❌ You are not authorized to use this command.")
        return

    subscription_data = read_subscription_data()

    if subscription_data:
        users_list = "\n".join(
            [f"{idx + 1}. User ID: `{user[0]}`, Expiration Date: `{user[1]}`" for idx, user in enumerate(subscription_data)]
        )
        await message.reply_text(f"**👥 Current Subscribed Users:**\n\n{users_list}")
    else:
        await message.reply_text("ℹ️ No users found in the subscription data.")

# 3. /myplan
@bot.on_message(filters.command("myplan") & filters.private)
async def my_plan(client, message: Message):
    user_id = str(message.from_user.id)
    subscription_data = read_subscription_data()  # Make sure this function is implemented elsewhere

    # Define YOUR_ADMIN_ID somewhere in your code
    if user_id == str(YOUR_ADMIN_ID):  # YOUR_ADMIN_ID should be an integer
        await message.reply_text("**✨ You have permanent access!**")
    elif any(user[0] == user_id for user in subscription_data):  # Assuming subscription_data is a list of [user_id, expiration_date]
        expiration_date = next(user[1] for user in subscription_data if user[0] == user_id)
        await message.reply_text(
            f"**📅 Your Premium Plan Status**\n\n"
            f"**🆔 User ID**: `{user_id}`\n"
            f"**⏳ Expiration Date**: `{expiration_date}`\n"
            f"**🔒 Status**: *Active*"
        )
    else:
        await message.reply_text("**❌ You are not a premium user.**")

# Channels data functions
def read_channels_data():
    if not os.path.exists("channels.txt"):
        return []
    with open("channels.txt", "r") as f:
        return [line.strip() for line in f.readlines()]

def write_channels_data(data):
    with open("channels.txt", "w") as f:
        for channel in data:
            f.write(channel + "\n")

# 4. /add_channel
@bot.on_message(filters.command("add_channel"))
async def add_channel(client, message: Message):
    user_id = str(message.from_user.id)
    subscription_data = read_subscription_data()

    if not any(user[0] == user_id for user in subscription_data):
        await message.reply_text("**❌ You are not a premium user.**")
        return

    try:
        _, channel_id = message.text.split()
        channels = read_channels_data()
        if channel_id not in channels:
            channels.append(channel_id)
            write_channels_data(channels)
            await message.reply_text(f"Channel/Group ID {channel_id} Added Successfully.")
        else:
            await message.reply_text(f"Channel/Group ID {channel_id} Is Already Added.")
    except ValueError:
        await message.reply_text("Invalid command format. Use: /add_channel {channel/group_id}")


# 5. /remove_channels
@bot.on_message(filters.command("remove_channel"))
async def remove_channel(client, message: Message):
    user_id = str(message.from_user.id)
    subscription_data = read_subscription_data()

    if not any(user[0] == user_id for user in subscription_data):
        await message.reply_text("**❌ You are not a premium user.**")
        return

    try:
        _, channel_id = message.text.split()
        channels = read_channels_data()
        if channel_id in channels:
            channels.remove(channel_id)
            write_channels_data(channels)
            await message.reply_text(f"Channel {channel_id} Removed Successfully.")
        else:
            await message.reply_text(f"Channel {channel_id} is not in the list.")
    except ValueError:
        await message.reply_text("Invalid command format. Use: /remove_channels {channel/group_id}")

# Command to show all allowed channels (Admin only)
@bot.on_message(filters.command("allowed_channels"))
async def allowed_channels(client, message: Message):
    user_id = message.from_user.id

    if not is_admin(user_id):
        await message.reply_text("❌ It's Only Owner Command.")
        return

    channels = read_channels_data()
    if channels:
        channels_list = "\n".join([f"- {channel}" for channel in channels])
        await message.reply_text(f"**📋 Allowed Channels/Groups:**\n\n{channels_list}")
    else:
        await message.reply_text("ℹ️ No Channels/Groups are currently allowed.")

# Command to remove all channels (Admin only)
@bot.on_message(filters.command("remove_all_channels"))
async def remove_all_channels(client, message: Message):
    user_id = message.from_user.id

    if not is_admin(user_id):
        await message.reply_text("❌ It's Only Owner Command.")
        return

    # Clear the channels data
    write_channels_data([])
    await message.reply_text("✅ **All Channels/Groups have been removed successfully.**")

@bot.on_message(filters.command("stop"))                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
async def restart_handler(_, m):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    await m.reply_text("🚦**STOPPED**🚦", True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    os.execl(sys.executable, sys.executable, *sys.argv)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

# PW Direct Download Command
@bot.on_message(filters.command("pwdl"))
async def pw_direct_download(bot: Client, m: Message):
    # Premium check
    user_id = str(m.from_user.id)
    subscription_data = read_subscription_data()
    if not any(user[0] == user_id for user in subscription_data):
        await m.reply_text("❌ You are not a premium user. Please upgrade your subscription! 💎")
        return
    
    await m.reply_text("🔐 **Starting PW Direct Download Process...**")
    
    try:
        # Step 1: PW Login
        query_msg = await bot.ask(
            chat_id=m.chat.id,
            text="🔐 **Enter your PW Mobile No. (without country code) or your Login Token:**"
        )
        
        user_input = query_msg.text.strip()

        if user_input.isdigit():
            mob = user_input
            payload = {
                "username": mob,
                "countryCode": "+91",
                "organizationId": "5eb393ee95fab7468a79d189"
            }
            headers = {
                "client-id": "5eb393ee95fab7468a79d189",
                "client-version": "12.84",
                "Client-Type": "MOBILE",
                "randomId": "e4307177362e86f1",
                "Accept": "application/json, text/plain, */*",
                "Content-Type": "application/json"
            }
            
            await m.reply_text("🔄 **Sending OTP... Please wait!**")
            otp_response = requests.post(
                "https://api.penpencil.co/v1/users/get-otp?smsType=0", 
                headers=headers, 
                json=payload
            ).json()

            if not otp_response.get("success"):
                await m.reply_text("❌ **Invalid Mobile Number! Please provide a valid PW login number.**")
                return
            
            await m.reply_text("✅ **OTP sent successfully! Please enter your OTP:**")
            otp_msg = await bot.ask(m.chat.id, text="🔑 **Enter the OTP you received:**")
            otp = otp_msg.text.strip()

            token_payload = {
                "username": mob,
                "otp": otp,
                "client_id": "system-admin",
                "client_secret": "KjPXuAVfC5xbmgreETNMaL7z",
                "grant_type": "password",
                "organizationId": "5eb393ee95fab7468a79d189",
                "latitude": 0,
                "longitude": 0
            }
            
            await m.reply_text("🔄 **Verifying OTP... Please wait!**")
            token_response = requests.post(
                "https://api.penpencil.co/v3/oauth/token", 
                data=token_payload
            ).json()
            
            token = token_response.get("data", {}).get("access_token")
            if not token:
                await m.reply_text("❌ **Login failed! Invalid OTP.**")
                return
            
            # Store token for this user
            user_tokens[m.from_user.id] = token
            
        elif user_input.startswith("e"):
            token = user_input
            # Store token for this user
            user_tokens[m.from_user.id] = token
        else:
            await m.reply_text("❌ **Invalid input! Please provide a valid mobile number or token.**")
            return

        headers = {
            "client-id": "5eb393ee95fab7468a79d189",
            "client-type": "WEB",
            "Authorization": f"Bearer {token}",
            "client-version": "3.3.0",
            "randomId": "04b54cdb-bf9e-48ef-974d-620e21bd3e23",
            "Accept": "application/json, text/plain, */*"
        }
        
        # Step 2: Get Batches
        batch_response = requests.get(
            "https://api.penpencil.co/v3/batches/my-batches?mode=1&amount=paid&page=1", 
            headers=headers
        ).json()
        
        batches = batch_response.get("data", [])
        if not batches:
            await m.reply_text("❌ **No batches found for this account.**")
            return

        # Create inline keyboard for batch selection
        keyboard = []
        for batch in batches:
            bi = batch.get("_id")
            bn = batch.get("name")
            keyboard.append([InlineKeyboardButton(bn, callback_data=f"pwdl_batch_{bi}")])
        
        # Add "All Batches" button
        keyboard.append([InlineKeyboardButton("📚 All Batches", callback_data="pwdl_all_batches")])
        
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await m.reply_text(
            "📚 **Select a batch to extract:**",
            reply_markup=reply_markup
        )

    except Exception as e:
        await m.reply_text(f"❌ **An error occurred:** `{str(e)}`")
        
@bot.on_callback_query(filters.regex(r"^pwdl_"))
async def handle_pwdl_batch_selection(bot, callback_query):
    try:
        data = callback_query.data
        user_id = callback_query.from_user.id
        
        if user_id not in user_tokens:
            await callback_query.message.edit_text("❌ **Session expired. Please login again using /pwdl command.**")
            return
            
        token = user_tokens[user_id]
        
        if data == "pwdl_all_batches":
            await callback_query.message.edit_text("🔄 **Starting extraction for all batches...**")
            await extract_all_batches_pwdl(bot, callback_query.message, token, user_id)
        else:
            batch_id = data.split("_")[2]
            await callback_query.message.edit_text(f"🔄 **Starting extraction for selected batch...**")
            await extract_single_batch_pwdl(bot, callback_query.message, batch_id, token, user_id)
    except Exception as e:
        await callback_query.message.edit_text(f"❌ **Error:** `{str(e)}`")

async def extract_single_batch_pwdl(bot, message, batch_id, token, user_id):
    try:
        headers = {
            "client-id": "5eb393ee95fab7468a79d189",
            "client-type": "WEB",
            "Authorization": f"Bearer {token}",
            "client-version": "3.3.0",
            "randomId": "04b54cdb-bf9e-48ef-974d-620e21bd3e23",
            "Accept": "application/json, text/plain, */*"
        }
        
        # Get batch details
        batch_details = requests.get(
            f"https://api.penpencil.co/v3/batches/{batch_id}/details", 
            headers=headers
        ).json()
        
        batch_name = batch_details.get("data", {}).get("name", "Unknown Batch")
        subjects = batch_details.get("data", {}).get("subjects", [])
        
        filename = f"{batch_name.replace('/', '_').replace(':', '_').replace('|', '_')}.txt"
        
        await bot.send_message(
            chat_id=message.chat.id, 
            text=f"🕵️ **Fetching details for Batch:** **{batch_name}**... Please wait!"
        )
        
        with open(filename, 'w', encoding='utf-8') as f:
            for subject in subjects:
                subject_id = subject.get("_id")
                subject_name = subject.get("subject")
                
                await bot.send_message(
                    chat_id=message.chat.id, 
                    text=f"📘 **Processing Subject:** **{subject_name}**... ⏳"
                )
                
                # Get topics with pagination
                page = 1
                while True:
                    topics_url = f"https://api.penpencil.co/batch-service/v1/batch-tags/{batch_id}/subject/{subject_id}/topics?page={page}&batchTagType=UNITS&limit=20"
                    topics_response = requests.get(topics_url, headers=headers).json()
                    
                    topics_data = topics_response.get("data", [])
                    if not topics_data:
                        break
                    
                    for topic in topics_data:
                        topic_id = topic.get("_id")
                        topic_name = topic.get("name")
                        
                        await bot.send_message(
                            chat_id=message.chat.id, 
                            text=f"📝 **Processing Topic:** **{topic_name}**... ⏳"
                        )
                        
                        # Get content for this topic
                        content_url = f"https://api.penpencil.co/batch-service/v3/batch-subject-schedules/{batch_id}/subject/{subject_id}/contents?skip=0&limit=20&contentType=LECTURES&tagId={topic_id}"
                        content_response = requests.get(content_url, headers=headers).json()
                        
                        content_data = content_response.get("data", [])
                        for content in content_data:
                            if content.get("type") == "LECTURE":
                                lecture_id = content.get("_id")
                                lecture_data = content.get("data", {})
                                video_details = lecture_data.get("videoDetails", {})
                                video_name = video_details.get("name", "").replace(":", "_")
                                
                                # Get video URL
                                video_url_response = requests.get(
                                    f"https://api.penpencil.co/v1/videos/video-url-details?type=BATCHES&videoContainerType=DASH&reqType=query&childId={lecture_id}&parentId={batch_id}&clientVersion=201",
                                    headers=headers
                                ).json()
                                
                                if video_url_response.get("success"):
                                    video_data = video_url_response.get("data", {})
                                    video_url = video_data.get("url", "")
                                    signed_url = video_data.get("signedUrl", "")
                                    
                                    if video_url and signed_url:
                                        full_video_url = video_url + signed_url
                                        f.write(f"{video_name}:{full_video_url}\n")
                                
                                # Extract homework attachments
                                for homework in lecture_data.get("homeworkIds", []):
                                    for attachment in homework.get("attachmentIds", []):
                                        name = attachment.get("name", "").replace(":", "_")
                                        base_url = attachment.get("baseUrl", "")
                                        key = attachment.get("key", "")
                                        if key:
                                            f.write(f"{name}:{base_url}{key}\n")
                    
                    # Check if there are more pages
                    if len(topics_data) < 20:
                        break
                    page += 1
        
        # Store extracted file path for download process
        current_extracted_file[user_id] = filename
        
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"✅ **Batch extraction completed!**\n\n📁 **File:** `{filename}`\n\n🚀 **Starting download process...**"
        )
        
        # Automatically start download process
        await start_download_process(bot, message, filename, user_id)
        
    except Exception as e:
        await message.reply_text(f"❌ **An error occurred during extraction:** `{str(e)}`")

async def extract_all_batches_pwdl(bot, message, token, user_id):
    try:
        headers = {
            "client-id": "5eb393ee95fab7468a79d189",
            "client-type": "WEB",
            "Authorization": f"Bearer {token}",
            "client-version": "3.3.0",
            "randomId": "04b54cdb-bf9e-48ef-974d-620e21bd3e23",
            "Accept": "application/json, text/plain, */*"
        }
        
        batch_response = requests.get(
            "https://api.penpencil.co/v3/batches/my-batches?mode=1&amount=paid&page=1", 
            headers=headers
        ).json()
        
        batches = batch_response.get("data", [])
        
        all_batches_filename = f"ALL_BATCHES_{user_id}.txt"
        
        with open(all_batches_filename, 'w', encoding='utf-8') as master_file:
            for batch in batches:
                batch_id = batch.get("_id")
                batch_name = batch.get("name")
                
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"🔄 **Extracting batch:** **{batch_name}**..."
                )
                
                # Extract single batch to temporary file
                temp_filename = f"temp_{batch_id}.txt"
                await extract_single_batch_to_file(bot, batch_id, token, temp_filename)
                
                # Append to master file
                with open(temp_filename, 'r', encoding='utf-8') as temp_file:
                    master_file.write(temp_file.read())
                    master_file.write("\n")
                
                # Clean up temp file
                if os.path.exists(temp_filename):
                    os.remove(temp_filename)
        
        # Store extracted file path for download process
        current_extracted_file[user_id] = all_batches_filename
        
        await bot.send_message(
            chat_id=message.chat.id,
            text=f"✅ **All batches extraction completed!**\n\n📁 **File:** `{all_batches_filename}`\n\n🚀 **Starting download process...**"
        )
        
        # Automatically start download process
        await start_download_process(bot, message, all_batches_filename, user_id)
            
    except Exception as e:
        await message.reply_text(f"❌ **An error occurred during batch extraction:** `{str(e)}`")

async def extract_single_batch_to_file(bot, batch_id, token, filename):
    """Extract single batch to file without starting download"""
    headers = {
        "client-id": "5eb393ee95fab7468a79d189",
        "client-type": "WEB",
        "Authorization": f"Bearer {token}",
        "client-version": "3.3.0",
        "randomId": "04b54cdb-bf9e-48ef-974d-620e21bd3e23",
        "Accept": "application/json, text/plain, */*"
    }
    
    batch_details = requests.get(
        f"https://api.penpencil.co/v3/batches/{batch_id}/details", 
        headers=headers
    ).json()
    
    batch_name = batch_details.get("data", {}).get("name", "Unknown Batch")
    subjects = batch_details.get("data", {}).get("subjects", [])
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(f"# Batch: {batch_name}\n")
        
        for subject in subjects:
            subject_id = subject.get("_id")
            subject_name = subject.get("subject")
            
            # Get topics with pagination
            page = 1
            while True:
                topics_url = f"https://api.penpencil.co/batch-service/v1/batch-tags/{batch_id}/subject/{subject_id}/topics?page={page}&batchTagType=UNITS&limit=20"
                topics_response = requests.get(topics_url, headers=headers).json()
                
                topics_data = topics_response.get("data", [])
                if not topics_data:
                    break
                
                for topic in topics_data:
                    topic_id = topic.get("_id")
                    topic_name = topic.get("name")
                    
                    # Get content for this topic
                    content_url = f"https://api.penpencil.co/batch-service/v3/batch-subject-schedules/{batch_id}/subject/{subject_id}/contents?skip=0&limit=20&contentType=LECTURES&tagId={topic_id}"
                    content_response = requests.get(content_url, headers=headers).json()
                    
                    content_data = content_response.get("data", [])
                    for content in content_data:
                        if content.get("type") == "LECTURE":
                            lecture_id = content.get("_id")
                            lecture_data = content.get("data", {})
                            video_details = lecture_data.get("videoDetails", {})
                            video_name = video_details.get("name", "").replace(":", "_")
                            
                            # Get video URL
                            video_url_response = requests.get(
                                f"https://api.penpencil.co/v1/videos/video-url-details?type=BATCHES&videoContainerType=DASH&reqType=query&childId={lecture_id}&parentId={batch_id}&clientVersion=201",
                                headers=headers
                            ).json()
                            
                            if video_url_response.get("success"):
                                video_data = video_url_response.get("data", {})
                                video_url = video_data.get("url", "")
                                signed_url = video_data.get("signedUrl", "")
                                
                                if video_url and signed_url:
                                    full_video_url = video_url + signed_url
                                    f.write(f"{video_name}:{full_video_url}\n")
            
                # Check if there are more pages
                if len(topics_data) < 20:
                    break
                page += 1

async def start_download_process(bot, m, extracted_file, user_id):
    """Start the download process with extracted file"""
    try:
        # Set the extracted file as input for download process
        y = extracted_file
        
        # Get batch name from filename
        file_name = os.path.splitext(os.path.basename(y))[0]
        
        path = f"./downloads/{m.chat.id}"

        try:
           with open(y, "r") as f:
               content = f.read()
           content = content.split("\n")
           links = []
           for i in content:
               if i.strip() and ":" in i:
                   links.append(i.split(":", 1))
           # Don't remove the file yet, we'll remove it after download
           # print(len(links)
        except Exception as e:
           await m.reply_text(f"Invalid file input: {str(e)}")
           return

        await m.reply_text(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **1**")
        input0: Message = await bot.listen(m.chat.id)
        raw_text = input0.text
        await input0.delete(True)

        await m.reply_text("**Enter Batch Name Or /d for default**")
        input1: Message = await bot.listen(m.chat.id)
        raw_text0 = input1.text
        await input1.delete(True)
        if raw_text0 == '/d':
            b_name = file_name
        else:
            b_name = raw_text0

        await m.reply_text("**Enter resolution** `144` , `240` , `360` , `480` , `720` , `1080`")
        input2: Message = await bot.listen(m.chat.id)
        raw_text2 = input2.text
        await input2.delete(True)
        try:
            if raw_text2 == "144":
                res = "256x144"
            elif raw_text2 == "240":
                res = "426x240"
            elif raw_text2 == "360":
                res = "640x360"
            elif raw_text2 == "480":
                res = "854x480"
            elif raw_text2 == "720":
                res = "1280x720"
            elif raw_text2 == "1080":
                res = "1920x1080"
            else:
                res = "1280x720"
        except Exception:
                res = "UN"

        await m.reply_text("**Enter A Caption For your Upload OR /d for default**")
        input3: Message = await bot.listen(m.chat.id)
        raw_text3 = input3.text
        await input3.delete(True)
        if raw_text3 == '/d':
            MR = "🅱🅴🅰🆂🆃 👑"
        else:
            MR = raw_text3

        await m.reply_text("**Enter pw token for mpd or /d for no **")
        input11: Message = await bot.listen(m.chat.id)
        token = input11.text
        await input11.delete(True)

        # NEW: Ask for HLS conversion preference
        await m.reply_text("**Enable HLS conversion for MPD? (yes/no)**\n\n- **yes**: Convert MPD to M3U8 (faster download)\n- **no**: Use DRM decryption (requires key)")
        input_hls: Message = await bot.listen(m.chat.id)
        hls_preference = input_hls.text.lower()
        await input_hls.delete(True)
        enable_hls = hls_preference in ['yes', 'y', '1', 'true']

        await m.reply_text("Enter Your Tumbnail Link or use `no` for default")
        input6: Message = await bot.listen(m.chat.id)
        thumb_input = input6.text.strip()
        await input6.delete(True)

        if thumb_input.lower() == "no":
            thumb = "no"
        elif thumb_input.startswith("http://") or thumb_input.startswith("https://"):
            getstatusoutput(f"wget '{thumb_input}' -O 'thumb.jpg'")
            thumb = "thumb.jpg"
        else:
            thumb = "no"

        if len(links) == 1:
            count = 1
        else:
            count = int(raw_text)

        # Start downloading links with HLS preference and raw_text2
        await process_links_download(bot, m, links, count, b_name, res, MR, token, thumb, user_id, extracted_file, enable_hls, raw_text2, thumb_input)
        
    except Exception as e:
        await m.reply_text(f"❌ Error starting download process: {str(e)}")

async def process_links_download(bot, m, links, count, b_name, res, MR, token, thumb, user_id, extracted_file, enable_hls=True, raw_text2=None, thumb_input=None):
    """Process the links for download with HLS preference"""
    try:
        for i in range(count - 1, len(links)):
            if not links[i] or len(links[i]) < 2:
                continue
                
            name1 = links[i][0].replace("\t", "").replace(":", "").replace("/", "").replace("+", "").replace("#", "").replace("|", "").replace("@", "").replace("*", "").replace(".", "").replace("https", "").replace("http", "").strip()
            name = f'{name1[:60]}🅱🅴🅰🆂🆃 👑'
            
            url = links[i][1].strip()
            
            if not url:
                continue

            # Handle different URL types
            if "visionias" in url:
                async with ClientSession() as session:
                    async with session.get(url, headers={'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'Accept-Language': 'en-US,en;q=0.9', 'Cache-Control': 'no-cache', 'Connection': 'keep-alive', 'Pragma': 'no-cache', 'Referer': 'http://www.visionias.in/', 'Sec-Fetch-Dest': 'iframe', 'Sec-Fetch-Mode': 'navigate', 'Sec-Fetch-Site': 'cross-site', 'Upgrade-Insecure-Requests': '1', 'User-Agent': 'Mozilla/5.0 (Linux; Android 12; RMX2121) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36', 'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': '"Android"',}) as resp:
                            text = await resp.text()
                            url = re.search(r"(https://.*?playlist.m3u8.*?)\"", text).group(1)
            
            elif "https://cpvod.testbook.com/" in url:
                url = url.replace("https://cpvod.testbook.com/","https://media-cdn.classplusapp.com/drm/")
                url = 'https://dragoapi.vercel.app/classplus?link=' + url
                mpd, keys = helper.get_mps_and_keys(url)
                url = mpd
                keys_string = " ".join([f"--key {key}" for key in keys])

            elif "d1d34p8vz63oiq" in url or "sec1.pw.live" in url:
                url = f"https://anonymouspwplayer-b99f57957198.herokuapp.com/pw?url={url}?token={token}"

            elif "acecwply" in url:
                cmd = f'yt-dlp -o "{name}.%(ext)s" -f "bestvideo[height<={raw_text2}]+bestaudio" --hls-prefer-ffmpeg --no-keep-video --remux-video mkv --no-warning "{url}"'

            elif "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3MjQyMzg3OTEsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiZEUxbmNuZFBNblJqVEROVmFWTlFWbXhRTkhoS2R6MDkiLCJmaXJzdF9uYW1lIjoiYVcxV05ITjVSemR6Vm10ak1WUlBSRkF5ZVNzM1VUMDkiLCJlbWFpbCI6Ik5Ga3hNVWhxUXpRNFJ6VlhiR0ppWTJoUk0wMVdNR0pVTlU5clJXSkRWbXRMTTBSU2FHRnhURTFTUlQwPSIsInBob25lIjoiVUhVMFZrOWFTbmQ1ZVcwd1pqUTViRzVSYVc5aGR6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJOalZFYzBkM1IyNTBSM3B3VUZWbVRtbHFRVXAwVVQwOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoiUShBbmRyb2lkIDEwLjApIiwiZGV2aWNlX21vZGVsIjoiU2Ftc3VuZyBTTS1TOTE4QiIsInJlbW90ZV9hZGRyIjoiNTQuMjI2LjI1NS4xNjMsIDU0LjIyNi4yNTUuMTYzIn19.snDdd-PbaoC42OUhn5SJaEGxq0VzfdzO49WTmYgTx8ra_Lz66GySZykpd2SxIZCnrKR6-R10F5sUSrKATv1CDk9ruj_ltCjEkcRq8mAqAytDcEBp72-W0Z7DtGi8LdnY7Vd9Kpaf499P-y3-godolS_7ixClcYOnWxe2nSVD5C9c5HkyisrHTvf6NFAuQC_FD3TzByldbPVKK0ag1UnHRavX8MtttjshnRhv5gJs5DQWj4Ir_dkMcJ4JaVZO3z8j0OxVLjnmuaRBujT-1pavsr1CCzjTbAcBvdjUfvzEhObWfA1-Vl5Y4bUgRHhl1U-0hne4-5fF0aouyu71Y6W0eg'
                url = url.split("bcov_auth")[0]+bcov 

            elif "classplusapp.com/drm/" in url:
                url = 'https://dragoapi.vercel.app/classplus?link=' + url
                mpd, keys = helper.get_mps_and_keys(url)
                url = mpd
                keys_string = " ".join([f"--key {key}" for key in keys])

            elif "edge.api.brightcove.com" in url:
                bcov = 'bcov_auth=eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE3Mjg3MDIyMDYsImNvbiI6eyJpc0FkbWluIjpmYWxzZSwiYXVzZXIiOiJVMFZ6TkdGU2NuQlZjR3h5TkZwV09FYzBURGxOZHowOSIsImlkIjoiT0dweFpuWktabVl3WVdwRlExSXJhV013WVdvMlp6MDkiLCJmaXJzdF9uYW1lIjoiU0hCWVJFc3ZkbVJ0TVVSR1JqSk5WamN3VEdoYVp6MDkiLCJlbWFpbCI6ImNXbE5NRTVoTUd4NloxbFFORmx4UkhkWVV6bFhjelJTWWtwSlVVcHNSM0JDVTFKSWVGQXpRM2hsT0QwPSIsInBob25lIjoiYVhReWJ6TTJkWEJhYzNRM01uQjZibEZ4ZGxWR1p6MDkiLCJhdmF0YXIiOiJLM1ZzY1M4elMwcDBRbmxrYms4M1JEbHZla05pVVQwOSIsInJlZmVycmFsX2NvZGUiOiJla3RHYjJoYWRtcENXSFo0YTFsV2FEVlBaM042ZHowOSIsImRldmljZV90eXBlIjoiYW5kcm9pZCIsImRldmljZV92ZXJzaW9uIjoidXBwZXIgdGhhbiAzMSIsImRldmljZV9tb2RlbCI6IlhpYW9NaSBNMjAwN0oxN0MiLCJyZW1vdGVfYWRkciI6IjQ0LjIyMi4yNTMuODUifX0.k_419KObeIVpLO6BqHcg8MpnvEwDgm54UxPnY7rTUEu_SIjOaE7FOzez5NL9LS7LdI_GawTeibig3ILv5kWuHhDqAvXiM8sQpTkhQoGEYybx8JRFmPw_fyNsiwNxTZQ4P4RSF9DgN_yiQ61aFtYpcfldT0xG1AfamXK4JlneJpVOJ8aG_vOLm6WkiY-XG4PCj5u4C3iyur0VM1-j-EhwHmNXVCiCz5weXDsv6ccV6SqNW2j_Cbjia16ghgX61XeIyyEkp07Nyrp7GN4eXuxxHeKcoBJB-YsQ0OopSWKzOQNEjlGgx7b54BkmU8PbiwElYgMGpjRT9bLTf3EYnTJ_wA'
                url = url.split("bcov_auth")[0]+bcov

            elif "tencdn.classplusapp" in url:
                headers = {'Host': 'api.classplusapp.com', 'x-access-token': f'{token_cp}', 'user-agent': 'Mobile-Android', 'app-version': '1.4.37.1', 'api-version': '18', 'device-id': '5d0d17ac8b3c9f51', 'device-details': '2848b866799971ca_2848b8667a33216c_SDK-30', 'accept-encoding': 'gzip'}
                params = (('url', f'{url}'))
                response = requests.get('https://api.classplusapp.com/cams/uploader/video/jw-signed-url', headers=headers, params=params)
                url = response.json()['url']  

            elif 'videos.classplusapp' in url:
                url = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers={'x-access-token': f'{token_cp}'}).json()['url']

            elif 'media-cdn.classplusapp.com' in url or 'media-cdn-alisg.classplusapp.com' in url or 'media-cdn-a.classplusapp.com' in url: 
                headers = { 'x-access-token': f'{token_cp}',"X-CDN-Tag": "empty"}
                response = requests.get(f'https://api.classplusapp.com/cams/uploader/video/jw-signed-url?url={url}', headers=headers)
                url   = response.json()['url']

            elif 'encrypted.m' in url:
                appxkey = url.split('*')[1]
                url = url.split('*')[0]

            elif "allenplus" in url or "player.vimeo" in url :
                if "controller/videoplay" in url :
                    url0 = "https://player.vimeo.com/video/" + url.split("videocode=")[1].split("&videohash=")[0]
                    url = f"https://master-api-v3.vercel.app/allenplus-vimeo?url={url0}&authorization=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzkxOTMzNDE5NSIsInRnX3VzZXJuYW1lIjoi4p61IFtvZmZsaW5lXSIsImlhdCI6MTczODY5MjA3N30.SXzZ1MZcvMp5sGESj0hBKSghhxJ3k1GTWoBUbivUe1I"
                else:  
                    url = f"https://master-api-v3.vercel.app/allenplus-vimeo?url={url}&authorization=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzkxOTMzNDE5NSIsInRnX3VzZXJuYW1lIjoi4p61IFtvZmZsaW5lXSIsImlhdCI6MTczODY5MjA3N30.SXzZ1MZcvMp5sGESj0hBKSghhxJ3k1GTWoBUbivUe1I"

            elif url.startswith("https://videotest.adda247.com/"):
                if url.split("/")[3] != "demo":
                    url = f'https://videotest.adda247.com/demo/{url.split("https://videotest.adda247.com/")[1]}'

            # NEW: Handle master.mpd URLs with HLS preference
            elif 'master.mpd' in url:
                if enable_hls:
                    # Convert MPD to M3U8 (HLS ON)
                    try:
                        await m.reply_text("🔄 Converting MPD to M3U8...")
                        m3u8_content, m3u8_url = helper.convert_mpd_to_m3u8(url, raw_text2)
                        
                        # Temporary m3u8 file create karo
                        m3u8_filename = f"{name}_converted.m3u8"
                        with open(m3u8_filename, 'w') as f:
                            f.write(m3u8_content)
                        
                        # URL ko m3u8 file se replace karo
                        url = m3u8_filename
                        await m.reply_text("✅ MPD successfully converted to M3U8")
                        
                    except Exception as e:
                        await m.reply_text(f"❌ MPD to M3U8 conversion failed: {str(e)}")
                        continue
                else:
                    # Use DRM decryption with KID:KEY extraction (HLS OFF)
                    try:
                        await m.reply_text("🔐 Extracting DRM keys for ClearKey decryption...")
                        
                        # Extract KID:KEY using the API
                        key_api_url = "https://studyable.io/studyrays/bot-development/key.php"
                        post_data = {"video_url": url}
                        
                        response = requests.post(
                            key_api_url, 
                            data=post_data, 
                            headers={"Content-Type": "application/x-www-form-urlencoded"}
                        )
                        
                        if response.status_code == 200:
                            key_data = response.json()
                            if key_data.get("success"):
                                kid_key_pair = key_data["data"][0]  # Format: "KID:KEY"
                                await m.reply_text(f"✅ DRM keys extracted: `{kid_key_pair}`")
                                
                                # Parse KID and KEY
                                kid, key = kid_key_pair.split(":")
                                
                                # Use Classplus-style DRM download with extracted keys
                                keys_string = f"--key {kid}:{key}"
                                
                                # Set up for DRM download
                                mpd = url
                                path = f"./downloads/{m.chat.id}"
                                
                                # Use your existing DRM download function
                                Show = f"🔐 DRM Decryption Progress\n\n📈 Total Links: {len(links)}\n💥 Currently On: {str(count).zfill(3)}\n\n📩 Downloading with DRM Keys\n\n🧚🏻‍♂️ Title: {name}"
                                prog = await m.reply_text(Show)
                                
                                # Call your existing DRM download function
                                res_file = await helper.decrypt_and_merge_video(mpd, keys_string, path, name, raw_text2)
                                filename = res_file
                                
                                cc = f'**╭── ⋆⋅☆⋅⋆ ──╮**\n✦ **{str(count).zfill(3)}** ✦\n**╰── ⋆⋅☆⋅⋆ ──╯**\n\n🎭 **Title:** `{name1} 😎 .mkv`\n🖥️ **Resolution:** [{res}]\n\n📘 **Course:** `{b_name}`\n\n🚀 **Extracted By:** `{MR}`'
                                
                                await prog.delete(True)
                                await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                                count += 1
                                await asyncio.sleep(1)
                                continue
                                
                            else:
                                await m.reply_text("❌ Failed to extract DRM keys from API response")
                                continue
                        else:
                            await m.reply_text(f"❌ Key extraction API failed with status: {response.status_code}")
                            continue
                            
                    except Exception as e:
                        await m.reply_text(f"❌ DRM key extraction and decryption failed: {str(e)}")
                        continue

            # Determine yt-dlp format
            if "youtu" in url:
                ytf = f"b[height<={raw_text2}][ext=mp4]/bv[height<={raw_text2}][ext=mp4]+ba[ext=m4a]/b[ext=mp4]"
            else:
                ytf = f"b[height<={raw_text2}]/bv[height<={raw_text2}]+ba/b/bv+ba"

            if "jw-prod" in url:
                cmd = f'yt-dlp -o "{name}.mp4" "{url}"'
            else:
                cmd = f'yt-dlp -f "{ytf}" "{url}" -o "{name}.mp4"'

            try:
                cc = f'**╭── ⋆⋅☆⋅⋆ ──╮**\n✦ **{str(count).zfill(3)}** ✦\n**╰── ⋆⋅☆⋅⋆ ──╯**\n\n🎭 **Title:** `{name1} 😎 .mkv`\n🖥️ **Resolution:** [{res}]\n\n📘 **Course:** `{b_name}`\n\n🚀 **Extracted By:** `{MR}`'
                cc1 = f'**╭── ⋆⋅☆⋅⋆ ──╮**\n✦ **{str(count).zfill(3)}** ✦\n**╰── ⋆⋅☆⋅⋆ ──╯**\n\n🎭 **Title:** `{name1} 😎 .pdf`\n\n📘 **Course:** `{b_name}`\n\n🚀 **Extracted By:** `{MR}`'
                cc2 = f'**╭── ⋆⋅☆⋅⋆ ──╮**\n✦ **{str(count).zfill(3)}** ✦\n**╰── ⋆⋅☆⋅⋆ ──╯**\n\n🎭 **Title:** `{name1} 😎 .jpg`\n\n📘 **Course:** `{b_name}`\n\n🚀 **Extracted By:** `{MR}`'
                ccyt = f'**╭── ⋆⋅☆⋅⋆ ──╮**\n✦ **{str(count).zfill(3)}** ✦\n**╰── ⋆⋅☆⋅⋆ ──╯**\n\n🎭 **Title:** `{name1} 😎 .mkv`\n🎬 **Video Link:** {url}\n🖥️ **Resolution:** [{res}]\n\n📘 **Course:** `{b_name}`\n\n🚀 **Extracted By:** `{MR}`'

                # Agar DRM download ho chuka hai to next link pe jao
                if 'master.mpd' in links[i][1] and not enable_hls:
                    # DRM download already completed in the elif block above
                    continue

                # Handle different content types
                if "drive" in url:
                    try:
                        ka = await helper.download(url, name)
                        copy = await bot.send_document(chat_id=m.chat.id,document=ka, caption=cc1)
                        count+=1
                        os.remove(ka)
                        time.sleep(1)
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif ".zip" in url:
                    try:
                        cmd = f'yt-dlp -o "{name}.zip" "{url}"'
                        download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                        os.system(download_cmd)
                        copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.zip', caption=cc1)
                        count += 1
                        os.remove(f'{name}.zip')
                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        count += 1
                        pass

                elif 'pdf*' in url:
                    pdf_key = url.split('*')[1]
                    url = url.split('*')[0]
                    pdf_enc = await helper.download_and_decrypt_pdf(url, name, pdf_key)
                    copy = await bot.send_document(chat_id=m.chat.id, document=pdf_enc, caption=cc1)
                    count += 1
                    os.remove(pdf_enc)
                    continue

                elif ".pdf" in url:
                    try:
                        if "cwmediabkt99" in url:
                            time.sleep(2)
                            cmd = f'yt-dlp -o "{name}.pdf" "https://master-api-v3.vercel.app/cw-pdf?url={url}&authorization=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIojoiNzkxOTMzNDE5NSIsInRnX3VzZXJuYW1lIjoi4p61IFtvZmZsaW5lXSIsImlhdCI6MTczODY5MjA3N30.SXzZ1MZcvMp5sGESj0hBKSghhxJ3k1GTWoBUbivUe1I"'
                            download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                            os.system(download_cmd)
                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1)
                            count += 1
                            os.remove(f'{name}.pdf')

                        else:
                            cmd = f'yt-dlp -o "{name}.pdf" "{url}"'
                            download_cmd = f"{cmd} -R 25 --fragment-retries 25"
                            os.system(download_cmd)
                            copy = await bot.send_document(chat_id=m.chat.id, document=f'{name}.pdf', caption=cc1) 
                            count +=1
                            os.remove(f'{name}.pdf')

                    except FloodWait as e:
                        await m.reply_text(str(e))
                        time.sleep(e.x)
                        continue

                elif any(img in url.lower() for img in ['.jpeg', '.png', '.jpg']):
                    try:
                        subprocess.run(['wget', url, '-O', f'{name}.jpg'], check=True)
                        await bot.send_photo(
                            chat_id=m.chat.id,
                            caption = cc2,
                            photo= f'{name}.jpg',  )
                    except subprocess.CalledProcessError:
                        await m.reply_text("Failed to download the image. Please check the URL.")
                    except Exception as e:
                        await m.reply_text(f"An error occurred: {e}")
                    finally:
                        if os.path.exists(f'{name}.jpg'):
                            os.remove(f'{name}.jpg')

                elif "youtu" in url:
                    try:
                        await bot.send_photo(chat_id=m.chat.id, photo=photo, caption=ccyt)
                        count += 1
                    except Exception as e:
                        await m.reply_text(str(e))
                        await asyncio.sleep(1)
                        continue

                elif ".ws" in url and  url.endswith(".ws"):
                    try : 
                        await helper.pdf_download(f"{api_url}utkash-ws?url={url}&authorization={api_token}",f"{name}.html")
                        time.sleep(1)
                        await bot.send_document(chat_id=m.chat.id, document=f"{name}.html", caption=cc1)
                        os.remove(f'{name}.html')
                        count += 1
                        time.sleep(5)
                    except FloodWait as e:
                        await asyncio.sleep(e.x)
                        await m.reply_text(str(e))
                        continue

                elif 'encrypted.m' in url:  
                    Show = f"✈️ 𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒 ✈️\n\n┠ 📈 Total Links = {len(links)}\n┠ 💥 Currently On = {str(count).zfill(3)}\n\n**📩 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐈𝐍𝐆 📩**\n\n**🧚🏻‍♂️ Title** : {name}\n├── **Extention** : {MR}\n├── **Resolution** : {raw_text2}\n├── **Url** : `Kya karega URL dekh ke  BSDK 👻👻`\n├── **Thumbnail** : `{thumb_input}`\n├── **Bot Made By** : 🅱🅴🅰🆂🆃 👑" 
                    prog = await m.reply_text(Show)  
                    res_file = await helper.download_and_decrypt_video(url, cmd, name, appxkey)  
                    filename = res_file  

                    await prog.delete(True)  
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)  
                    count += 1  
                    await asyncio.sleep(1)  
                    continue  

                elif 'drmcdni' in url or 'drm/wv' in url:
                    Show = f"𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒 ✈️\n\n┠ 📈 Total Links = {len(links)}\n┠ 💥 Currently On = {str(count).zfill(3)}\n\n**📩 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐈𝐍𝐆 📩**\n\n**🧚🏻‍♂️ Title** : {name}\n├── **Extention** : {MR}\n├── **Resolution** : {raw_text2}\n├── **Url** : `Kya karega URL dekh ke  BSDK 👻👻`\n├── **Thumbnail** : `{thumb_input}`\n├── **Bot Made By** : 🅱🅴🅰🆂🆃 👑"
                    prog = await m.reply_text(Show)

                    # Use the decrypt_and_merge_video function
                    res_file = await helper.decrypt_and_merge_video(mpd, keys_string, path, name, raw_text2)

                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    await asyncio.sleep(1)
                    continue

                else:
                    Show = f"✈️ 𝐏𝐑𝐎𝐆𝐑𝐄𝐒𝐒 ✈️\n\n┠ 📈 Total Links = {len(links)}\n┠ 💥 Currently On = {str(count).zfill(3)}\n\n**📩 𝐃𝐎𝐖𝐍𝐋𝐎𝐀𝐃𝐈𝐍𝐆 📩**\n\n**🧚🏻‍♂️ Title** : {name}\n├── **Extention** : {MR}\n├── **Resolution** : {raw_text2}\n├── **Url** : `Kya karega URL dekh ke  BSDK 👻👻`\n├── **Thumbnail** : `{thumb_input}`\n├── **Bot Made By** : 🅱🅴🅰🆂🆃 👑"
                    prog = await m.reply_text(Show)
                    res_file = await helper.download_video(url, cmd, name)
                    filename = res_file
                    await prog.delete(True)
                    await helper.send_vid(bot, m, cc, filename, thumb, name, prog)
                    count += 1
                    time.sleep(1)

            except Exception as e:
                await m.reply_text(f"**downloading failed **\n\n{str(e)}\n\n**Name** - {name}\n**Link** - {url}")
                count += 1
                continue

        # Clean up extracted file after download completion
        if os.path.exists(extracted_file):
            os.remove(extracted_file)
        if user_id in current_extracted_file:
            del current_extracted_file[user_id]
            
        await m.reply_text("**Sᴜᴄᴄᴇsғᴜʟʟʏ Dᴏᴡɴʟᴏᴀᴅᴇᴅ Aʟʟ Lᴇᴄᴛᴜʀᴇs SIR 👿🚀**")
        
    except Exception as e:
        await m.reply_text(f"Error in download process: {str(e)}")
        # Clean up on error
        if os.path.exists(extracted_file):
            os.remove(extracted_file)
        if user_id in current_extracted_file:
            del current_extracted_file[user_id]

@bot.on_message(filters.command("drm")) # & filters.private)
async def account_login(bot: Client, m: Message):
    #if m.chat.type == "private":
    user_id = str(m.from_user.id)
    subscription_data = read_subscription_data()
    if not any(user[0] == user_id for user in subscription_data):
        await m.reply_text("❌ You are not a premium user. Please upgrade your subscription! 💎")
        return          
    editable = await m.reply_text("**Please Send TXT file for download**")
    input: Message = await bot.listen(editable.chat.id)
    y = await input.download()
    file_name, ext = os.path.splitext(os.path.basename(y))  # Extract filename & extension

    if file_name.endswith("_helper"):  # ✅ Check if filename ends with "_helper"
        x = decrypt_file_txt(y)  # Decrypt the file
        await input.delete(True)
    else:
        x = y 

    path = f"./downloads/{m.chat.id}"

    try:
       with open(x, "r") as f:
           content = f.read()
       content = content.split("\n")
       links = []
       for i in content:
           links.append(i.split("://", 1))
       os.remove(x)
            # print(len(links)
    except:
           await m.reply_text("Invalid file input.")
           os.remove(x)
           return                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

    await editable.edit(f"Total links found are **{len(links)}**\n\nSend From where you want to download initial is **1**")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    input0: Message = await bot.listen(editable.chat.id)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    raw_text = input0.text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    await input0.delete(True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

    await editable.edit("**Enter Batch Name Or /d for default**")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    input1: Message = await bot.listen(editable.chat.id)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    raw_text0 = input1.text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    await input1.delete(True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    if raw_text0 == '/d':                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        b_name = file_name                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                
    else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        b_name = raw_text0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

    await editable.edit("**Enter resolution** `144` , `240` , `360` , `480` , `720` , `1080`")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    input2: Message = await bot.listen(editable.chat.id)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    raw_text2 = input2.text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    await input2.delete(True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    try:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        if raw_text2 == "144":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            res = "256x144"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        elif raw_text2 == "240":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            res = "426x240"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        elif raw_text2 == "360":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            res = "640x360"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        elif raw_text2 == "480":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            res = "854x480"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        elif raw_text2 == "720":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            res = "1280x720"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        elif raw_text2 == "1080":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
            res = "1920x1080"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
            res = "1280x720"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    except Exception:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
            res = "UN"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

    await editable.edit("**Enter A Caption For your Upload OR /d for default**")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    input3: Message = await bot.listen(editable.chat.id)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    raw_text3 = input3.text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    await input3.delete(True)
    if raw_text3 == '/d':                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        MR = "🅱🅴🅰🆂🆃 👑"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        MR = raw_text3

    await editable.edit("**Enter pw token for mpd or /d for no **")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    input11: Message = await bot.listen(editable.chat.id)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    token = input11.text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    await input11.delete(True)

    # NEW: Ask for HLS conversion preference
    await editable.edit("**Enable HLS conversion for MPD? (yes/no)**\n\n- **yes**: Convert MPD to M3U8 (faster download)\n- **no**: Use DRM decryption (requires key)")
    input_hls: Message = await bot.listen(editable.chat.id)
    hls_preference = input_hls.text.lower()
    await input_hls.delete(True)
    enable_hls = hls_preference in ['yes', 'y', '1', 'true']

    await editable.edit("Enter Your Tumbnail Link or use `no` for default")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    input6 = message = await bot.listen(editable.chat.id)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    raw_text6 = input6.text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    await input6.delete(True)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    await editable.delete()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

    thumb = input6.text                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    if thumb.startswith("http://") or thumb.startswith("https://"):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        getstatusoutput(f"wget '{thumb}' -O 'thumb.jpg'")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        thumb = "thumb.jpg"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        thumb == "no"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

    if len(links) == 1:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        count = 1                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
    else:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  
        count = int(raw_text)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  

    # Start downloading using the same process_links_download function with HLS preference and raw_text2
    await process_links_download(bot, m, links, count, b_name, res, MR, token, thumb, m.from_user.id, x, enable_hls, raw_text2, raw_text6)

bot.run()