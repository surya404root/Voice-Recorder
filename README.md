# 🎙️ Voice Recorder

<p align="center">
  <img src="https://images.unsplash.com/photo-1589903308904-1010c2294adc?auto=format&fit=crop&w=1200&q=80" width="100%" alt="Voice Recorder Banner"/>
</p>

<p align="center">
  A lightweight, efficient, and modern Android Voice Recorder application
  built with Kotlin and designed for smooth performance across development
  environments including Android Studio, Linux, and Termux.
</p>

---

## 📌 Overview

**Voice Recorder** is a high-quality audio recording application built for Android.  
It provides a clean interface, reliable recording functionality, and structured code architecture suitable for learning and production-level improvements.

This project is compatible with:

- Android Studio (GUI-based development)
- Linux (CLI-based build using Gradle)
- Termux (Android terminal environment)

---

## ✨ Features

- 🎤 High-quality audio recording (MediaRecorder API)
- ▶️ Built-in playback support (MediaPlayer API)
- ⏸ Pause / Resume functionality
- 📂 Automatic file saving with timestamps
- 🗑 Easy file deletion
- ⚡ Optimized and lightweight performance
- 🧩 Clean project structure

---

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Kotlin | Core development language |
| Android SDK | Application framework |
| MediaRecorder API | Audio recording |
| MediaPlayer API | Playback |
| Gradle | Build automation |
| MVVM (Optional) | Scalable architecture |

---

# 🚀 Installation & Setup

---

## 🖥️ Method 1: Android Studio (Recommended)

### 1️⃣ Clone Repository

```bash
git clone https://github.com/surya404root/Voice-Recorder.git
cd Voice-Recorder
```
### 2️⃣ Open Project

• Open Android Studio

• Click Open

• Select the project folder

### 3️⃣ Sync Gradle

Allow Gradle to download dependencies.

### 4️⃣ Run

Connect device/emulator → Click Run ▶

## 🐧 Method 2: Linux (Command Line Build)

### 📌 Requirements

• OpenJDK 11 or higher

• Gradle (if wrapper not included)

• Android SDK installed

• ANDROID_HOME environment variable set

### Install Java (Ubuntu/Debian)
```
sudo apt update
sudo apt install openjdk-17-jdk
```
### Verify Java
```
java -version
```
### Build Project Using Gradle Wrapper
```
cd Voice-Recorder
chmod +x gradlew
./gradlew build
```
### Generate Debug APK
```
./gradlew assembleDebug
```
#### APK output location:
```
app/build/outputs/apk/debug/
```
## 📱 Method 3: Termux Setup (Advanced Users)

> ⚠ Note: Full Android builds inside Termux require SDK configuration and large storage.

### Step 1: Install Required Packages
```
pkg update
pkg upgrade
pkg install git openjdk-17
pkg install wget unzip
```
### Step 2: Clone Repository
```
git clone https://github.com/surya404root/Voice-Recorder.git
cd Voice-Recorder
```

### Step 3: Give Permission
```
chmod +x gradlew
```
