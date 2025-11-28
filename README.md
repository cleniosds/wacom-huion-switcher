# Using Wacom and Huion Tablets on the Same Windows PC

If you’ve ever used tablets from both **Wacom** and **Huion**, you’ve probably wondered whether it’s possible to use both on the same Windows computer.
The short answer is: **no, not at the same time**.

On Linux this is possible, but I didn’t explore that deeply.

In my setup I use a **Huion Kamvas 20** and a **Wacom One 13.3**, both pen displays, and I wanted to switch between them without reinstalling drivers every time.

After extensive testing, I created a working solution.

---

## 🖥️ My Setup

* Huion Kamvas 20
* Wacom One 13.3
* Both permanently connected
* HDMI splitter (but separate HDMI adapters also work)

---

## 📎 Program on GitHub

This tool allows you to automatically switch between:

* Wacom services
* Wintab DLLs for each brand

---

# 🛠️ How Everything Was Set Up

## 1️⃣ Fixing the Huion Pen Not Working in ZBrush

I had the Huion driver installed, but the pen **did not work inside ZBrush**.

**Fix:**

Go to:

```
C:\Program Files\HuionTablet\
```

Find `HuionTablet.exe`
Right-click → **Properties** → **Compatibility**
Enable **Run this program as an administrator**.

Restart the PC.
After that, the pen works correctly in ZBrush.

---

## 2️⃣ Preparing Huion’s Wintab DLLs

Inside the program directory, go to:

```
/Huion/
    /System32
    /SysWOW64
```

Copy the system DLLs:

### Copy from:

```
C:\Windows\System32\Wintab32.dll
```

to:

```
Huion/System32
```

Then:

```
C:\Windows\SysWOW64\Wintab32.dll
```

to:

```
Huion/SysWOW64
```

---

## 3️⃣ Disable Huion Auto-Startup

Open **Task Manager** → **Startup**
Disable any Huion entries.

Restart your PC.

---

## 4️⃣ Install the Wacom Driver (Without Removing Huion’s)

Do **not** uninstall the Huion driver.

After installing the Wacom driver, reboot.

Then repeat the DLL process in:

```
/Wacom/
    /System32
    /SysWOW64
```

Copy from:

```
C:\Windows\System32\Wintab32.dll
```

to:

```
Wacom/System32
```

And:

```
C:\Windows\SysWOW64\Wintab32.dll
```

to:

```
Wacom/SysWOW64
```

---

## 5️⃣ Change Wacom Service Startup Type

Open the Start Menu → type **Services**
Find:

```
Wacom Professional Service
```

Right-click → **Properties**
Set **Startup type** → **Manual**.

---

## 6️⃣ Disable Wacom Auto-Startup

Open **Task Manager** → **Startup**
Disable any Wacom entries.

---

# 🔄 Switching Between Wacom and Huion

In the root folder of this program you will find:

```
selector.bat
selector.py
servwacom.bat
servwacom.py
```

Both tablets must be connected and displaying an image before switching.

---

## 🔹 Using the Wacom

1. Run **servwacom.bat**
   Accept the admin prompt.

You will see something like:

```
=== Service Control ===
Service: WTabletServicePro
Current status: RUNNING

1 - Start service
2 - Stop service
0 - Exit
```

Select:

👉 **1 - Start service**

2. Run **selector.bat**
   Choose:

👉 **1 - Use Wacom DLL**

3. Open **Wacom Tablet Properties**.
   Your Wacom tablet is ready.

---

## 🔹 Using the Huion

1. Run **servwacom.bat**
   Choose:

👉 **2 - Stop service**

2. Run **selector.bat**
   Choose:

👉 **2 - Use Huion DLL**

3. Go to:

```
C:\Program Files\HuionTablet
```

Run **HuionTablet.exe**.

Your Huion tablet is now active.

---

# ⚠️ Important Notes

* When switching from Huion to Wacom, **close the Huion driver from the system tray first**.
* Always use **servwacom.bat** and **selector.bat** to switch.
* Do **not** uninstall either driver — both must remain installed.
