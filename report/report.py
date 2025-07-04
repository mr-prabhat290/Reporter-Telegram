import asyncio
import os
import platform
from telethon import TelegramClient, functions, types, errors
from prettytable import PrettyTable

# Terminal Color Setup
rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[94m', '\033[01;35m'
cn, k, g = '\033[00;36m', '\033[90m', '\033[38;5;130m'

# Display report options table
def show_menu():
    t = PrettyTable([f'{cn}Number{lrd}', f'{cn}Report Type{lrd}'])
    reasons = [
        "Spam", "Pornography", "Violence", "Child Abuse", "Other",
        "Copyright", "Fake", "Geo Irrelevant", "Illegal Drugs", "Personal Details"
    ]
    for i, reason in enumerate(reasons, 1):
        t.add_row([f'{lgn}{i}{lrd}', f'{gn}Report {reason}{lrd}'])
    print(t)

# Clear terminal screen
def clear():
    os.system("cls" if platform.system() == "Windows" else "clear")

# Main report runner
async def main():
    clear()
    print(f"{lrd}[{lgn}+{lrd}] {gn}Telegram Mass Reporter — Updated Version\n")

    api_id = int(input(f"{lrd}[{lgn}+{lrd}] {gn}Enter API ID: {g}"))
    api_hash = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter API Hash: {g}")
    phone = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter phone number (+91xxxxxxxxxx): {g}")
    password = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter 2FA password (if any): {g}")
    
    show_menu()
    method = input(f"{lrd}[{lgn}?{lrd}] {gn}Choose a report type (1-10): {g}")
    target = input(f"{lrd}[{lgn}+{lrd}] {gn}Enter target @username or user ID: {g}")
    count = int(input(f"{lrd}[{lgn}+{lrd}] {gn}How many times to report: {g}"))

    session_name = f"session_{phone.replace('+', '')}"

    try:
        client = TelegramClient(session_name, api_id, api_hash)
        await client.start(phone=phone, password=password)

        user = await client.get_entity(target)
        peer = types.InputPeerUser(user_id=user.id, access_hash=user.access_hash)

        # Define report reasons
        reasons = {
            "1": types.InputReportReasonSpam(),
            "2": types.InputReportReasonPornography(),
            "3": types.InputReportReasonViolence(),
            "4": types.InputReportReasonChildAbuse(),
            "5": types.InputReportReasonOther(),
            "6": types.InputReportReasonCopyright(),
            "7": types.InputReportReasonFake(),
            "8": types.InputReportReasonGeoIrrelevant(),
            "9": types.InputReportReasonIllegalDrugs(),
            "10": types.InputReportReasonPersonalDetails(),
        }

        if method not in reasons:
            print(f"{lrd}[{rd}!{lrd}] Invalid method selected.")
            return

        reason = reasons[method]

        for i in range(count):
            await client(functions.account.ReportPeerRequest(
                peer=peer,
                reason=reason,
                message="Reported by script."
            ))
            print(f"{lgn}[+]{lrd} Report {i + 1} sent.")

            # Wait 30-60 seconds between each to avoid bans
            await asyncio.sleep(30)

        print(f"\n{lrd}[{lgn}✓{lrd}] {gn}Finished sending {count} reports.")

    except errors.PhoneNumberBannedError:
        print(f"{lrd}[{rd}X{lrd}] {k}This phone number is banned from using Telegram API.")
    except Exception as e:
        print(f"{lrd}[{rd}ERROR{lrd}] {k}{str(e)}")
    finally:
        await client.disconnect()

# Run the async main
asyncio.run(main())
