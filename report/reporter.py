import asyncio
import os
import platform
from telethon import TelegramClient, functions, types, errors

# Color setup
rd, gn, lgn, lrd, k = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;31m', '\033[90m'

def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")

def show_methods():
    reasons = [
        "Spam", "Other", "Violence", "Pornography",
        "Copyright", "Fake", "Geo Irrelevant",
        "Illegal Drugs", "Personal Details"
    ]
    for i, reason in enumerate(reasons, 1):
        print(f"{lrd}[{lgn}{i}{lrd}] {gn}Report {reason}")

async def main():
    clear()
    print(f"{lrd}[{lgn}+{lrd}] {gn}Telegram Group Reporter (Public/Private Supported)")

    api_id = int(input(f"{lrd}[{lgn}+{lrd}] {gn}Enter API ID: {k}"))
    api_hash = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter API Hash: {k}")
    phone = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter phone (+91xxxx): {k}")
    password = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter 2FA password (if any, else press Enter): {k}")
    target = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter @group username or invite link or -100GroupID: {k}")

    show_methods()
    method = input(f"{lrd}[{lgn}?{lrd}] {gn}Select reason (1–9): {k}")
    count = int(input(f"{lrd}[{lgn}+{lrd}] {gn}How many times to report?: {k}"))

    session = f"group_session_{phone.replace('+','')}"
    client = TelegramClient(session, api_id, api_hash)

    try:
        await client.start(phone=phone, password=password)

        # Convert target to entity
        try:
            if target.startswith("https://t.me/"):
                target = target.split("/")[-1]
            entity = await client.get_entity(target)
        except:
            print(f"{rd}❌ Could not find or join the group.")
            return

        messages = await client.get_messages(entity, limit=3)
        message_ids = [msg.id for msg in messages]
        if not message_ids:
            print(f"{rd}❌ No recent messages to report.")
            return

        reasons = {
            "1": types.InputReportReasonSpam(),
            "2": types.InputReportReasonOther(),
            "3": types.InputReportReasonViolence(),
            "4": types.InputReportReasonPornography(),
            "5": types.InputReportReasonCopyright(),
            "6": types.InputReportReasonFake(),
            "7": types.InputReportReasonGeoIrrelevant(),
            "8": types.InputReportReasonIllegalDrugs(),
            "9": types.InputReportReasonPersonalDetails()
        }

        reason = reasons.get(method)
        if not reason:
            print(f"{rd}❌ Invalid report reason.")
            return

        print(f"{gn}📣 Starting report to group: {target}")
        for i in range(count):
            await client(functions.messages.ReportRequest(
                peer=entity,
                id=message_ids,
                reason=reason,
                message="Inappropriate content reported by user."
            ))
            print(f"{lgn}[✓] Report {i + 1} sent.")
            await asyncio.sleep(30)  # Delay to avoid ban

        print(f"\n{lrd}[{lgn}✓{lrd}] {gn}All reports completed successfully.")

    except errors.PhoneNumberBannedError:
        print(f"{rd}⚠️ This phone number is banned from Telegram API.")
    except Exception as e:
        print(f"{rd}⚠️ Error: {e}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
