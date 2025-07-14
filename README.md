# Kuchipudi-Hastas-Detector

An AI-powered Streamlit application designed to assist Kuchipudi dancers in learning and understanding the **Hastas** (hand gestures) used in this classical Indian dance form. The app takes a hand gesture as input and returns its **name**, **meaning**, and **explanation**. It is especially helpful for learners who struggle with memorizing the names, slokas, meanings, and the visual representations of these gestures.

---

##  Project Highlights

-  Detects **single-hand (Asamyukta Hastas)** and **double-hand (Samyukta Hastas)** gestures.
-  Provides **meanings and context** for each hasta.
-  Built with **Python 3.13** and **Streamlit** for a smooth and intuitive UI.
-  Designed to be extended with datasets and models — no dataset included in this repo.
-  No use of OpenCV or complex dependencies — clean and focused on logic and UI.

---

## 📸 Dataset Information

This repository **does not include a dataset**. You must use or collect a dataset that contains images of **Kuchipudi hand gestures** in various forms (clear, front-facing, and correctly labeled). Ideally, the dataset should have:

- High-resolution images
- Labeled gestures for both hands
- Balanced examples of all Hastas

---

## 💡 How It Works

The app uses a classification model to detect a given hand gesture from an uploaded image (once integrated with a dataset). It identifies the gesture and displays:

- The name of the gesture (in Sanskrit/English)
- Its classification (Asamyukta or Samyukta)
- The traditional sloka (if available)
- The symbolic meaning or usage in dance

---

##  Asamyukta Hastas (Single-Handed Gestures)

| No. | Hasta | Meaning |
|-----|-------|---------|
| 1   | Pataka | Flag – cloud, forest, denial |
| 2   | Tripataka | Three parts of a flag – crown, tree, lamp |
| 3   | Ardhapataka | Half flag – leaves, knife, board |
| 4   | Kartarimukha | Scissors – separation, opposition, death |
| 5   | Mayura | Peacock – bird, tilaka, vomiting |
| 6   | Ardhachandra | Half moon – moon, spear, waist |
| 7   | Arala | Bent – drinking nectar, poison |
| 8   | Shukatunda | Parrot's beak – shooting, spear |
| 9   | Mushti | Fist – strength, holding hair |
| 10  | Shikhara | Peak – bow, husband, pillar |
| 11  | Kapittha | Elephant apple – Lakshmi, Saraswati, milking cows |
| 12  | Katakamukha | Opening of a bracelet – plucking flowers, threading necklace |
| 13  | Suchi | Needle – number one, pointing, threatening |
| 14  | Chandrakala | Digit of moon – moon, face, spear |
| 15  | Padmakosha | Lotus bud – fruit, flower, ball |
| 16  | Sarpasirsha | Snake head – snake, water offering |
| 17  | Mrigashirsha | Deer head – deer, face, flute |
| 18  | Simhamukha | Lion face – lion, healing, elephant |
| 19  | Kangula | Bell – coconut, small bell |
| 20  | Alapadma | Lotus – beauty, full moon |
| 21  | Chatura | Clever – gold, eye, oil |
| 22  | Bhramara | Bee – bee, Krishna, cupid |
| 23  | Hamsasya | Swan beak – pearl, offering |
| 24  | Hamsapaksha | Swan wing – number six, construction |
| 25  | Samdamsha | Pinching – insect, burning |
| 26  | Mukula | Bud – lotus bud, eating, flower |
| 27  | Tamrachuda | Cock – rooster |
| 28  | Trishula | Trident – Shiva’s weapon |

---

##  Samyukta Hastas (Double-Handed Gestures)

| No. | Hasta | Meaning |
|-----|-------|---------|
| 1   | Anjali | Salutation – greeting deities, elders |
| 2   | Kapota | Pigeon – respectful approach |
| 3   | Karkata | Crab – gathering, twisting limbs |
| 4   | Swastika | Auspicious – symbol of good fortune |
| 5   | Dola | Swing – standing position |
| 6   | Pushpaputa | Flower basket – offerings, arati |
| 7   | Utsanga | Embrace – affection, teaching |
| 8   | Shivalinga | Lord Shiva – representation of Shiva |
| 9   | Katakavardhana | Chain – coronation, weddings |
| 10  | Kartariswastika | Crossed scissors – tree, creeper |
| 11  | Shakata | Demon face – Rakshasa |
| 12  | Shankha | Conch – blowing conch |
| 13  | Chakra | Discus – Vishnu’s weapon |
| 14  | Samputa | Container – secrecy, concealment |
| 15  | Pasha | Noose – love, enmity |
| 16  | Keelaka | Bond – affection |
| 17  | Matsya | Fish – representing fish |
| 18  | Kurma | Turtle – representing turtle |
| 19  | Varaha | Boar – representation of Varaha |
| 20  | Garuda | Eagle – vehicle of Vishnu |
| 21  | Nagabandha | Snake knot – couple, binding |
| 22  | Khatwa | Bed – bed, deathbed |
| 23  | Bherunda | Pair of birds – fierce bird |
| 24  | Avahitha | Modesty – concealment, shyness |

---

##  Usage Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Kuchipudi-Hastas-Detector.git
   cd Kuchipudi-Hastas-Detector

running?
python train_model.py
and after the training of the model only then
python classify_realtime.py


## 📸 Screenshot

Here's a preview of the application in action:

![App Screenshot](https://github.com/Srinidhi-Chitti/Kuchipudi-Hastas-Detector/blob/main/Screenshot%202025-07-14%20142305.png)
