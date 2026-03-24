# Bluetooth Low Energy with ESP32-C6

## Executive Summary
This class introduces **Bluetooth Low Energy (BLE)** as a short-range, low-power wireless technology for embedded systems using the **ESP32-C6**. The session covers BLE roles, discovery, connection flow, and the **GATT** data model of services and characteristics. Students then implement and verify a basic BLE peripheral on the ESP32-C6 using a scanner tool on a phone or PC. By the end of the class, students will be able to explain the BLE communication model, identify central and peripheral roles, interpret a simple GATT structure, and validate a working BLE application on real hardware.

---

## 1. Session Information

- **Session title:** Bluetooth Low Energy with ESP32-C6
- **Duration:** 2 hours
- **Format:** Face-to-face, instructor-led, with lab activity
- **Prerequisites:**
  - C/C++ programming
  - Basic ESP32 project structure
  - GPIO and timers
  - Serial debugging
  - Basic networking concepts

---

## 2. SMART Learning Outcomes

By the end of this session, students will be able to:

1. **Differentiate** Bluetooth Classic and BLE by identifying at least **three technical differences** related to power consumption, communication style, and typical use cases.
2. **Identify** the BLE roles of **central** and **peripheral**, and correctly classify at least **4 of 5 example devices**.
3. **Interpret** a simple BLE GATT structure by mapping the relationship among **service, characteristic, and properties**.
4. **Configure and run** an ESP32-C6 BLE peripheral that advertises its presence and exposes **one readable characteristic**.
5. **Verify** BLE operation using a scanner tool and document technical evidence in the lab log.

---

## 3. Why BLE Matters in Embedded Systems

**Bluetooth Low Energy (BLE)** is designed for:

- short-range wireless communication
- low power consumption
- small, structured data exchanges
- direct interaction with nearby devices

BLE is widely used in:

- wearable devices
- wireless sensors
- smart locks
- beacons
- portable medical devices
- local configuration interfaces

For embedded engineers, BLE is valuable because it provides a practical way to connect a device to a **smartphone, tablet, or nearby computer** without requiring complex network infrastructure.

---

## 4. Bluetooth Classic vs BLE

BLE is part of the Bluetooth family, but it is not the same as Bluetooth Classic.

| Feature | Bluetooth Classic | BLE |
|---|---:|---:|
| Typical use | Audio, continuous streaming | Sensors, control, low-rate data |
| Power consumption | Higher | Lower |
| Communication style | More continuous | Short bursts |
| Common embedded use | Less common | Very common |
| Typical examples | Headphones, speakers | Wearables, sensor nodes, beacons |

### Key point
BLE is not simply “Bluetooth but slower.” It uses a different interaction model optimized for efficient discovery and structured data exchange.

---

## 5. Core BLE Concepts

BLE communication is organized around four essential ideas:

### 5.1 Advertising
A device announces its presence by transmitting advertisement packets.

### 5.2 Scanning
Another device listens for nearby advertisements.

### 5.3 Connecting
After discovery, a device may initiate a connection for deeper interaction.

### 5.4 GATT Data Model
Once connected, data is usually exchanged through **services** and **characteristics**.

---

## 6. BLE Roles

### Peripheral
A **peripheral** is typically the embedded device that:

- advertises its presence
- exposes data or functions
- waits for a central device to connect

Examples:

- smart temperature sensor
- wearable monitor
- industrial beacon
- ESP32-C6 node

### Central
A **central** is typically the device that:

- scans for peripherals
- initiates the connection
- reads or writes data

Examples:

- smartphone
- tablet
- laptop
- commissioning tool

### Typical relation in this class
- **ESP32-C6** = Peripheral
- **Phone or PC scanner** = Central

---

## 7. BLE Communication Flow

A simplified BLE interaction usually follows this sequence:

1. The peripheral starts **advertising**.
2. The central starts **scanning**.
3. The central detects the advertiser.
4. The central optionally **connects**.
5. The central reads, writes, or subscribes to characteristics.

### Important distinction
- **Advertising** is discovery.
- **Connection** is a separate stage.
- A device may be visible before any connection exists.

---

## 8. GATT Model

The **Generic Attribute Profile (GATT)** is the main data model used by BLE applications.

### Service
A **service** groups related functionality.

Examples:
- battery service
- environmental sensing service
- custom sensor service

### Characteristic
A **characteristic** is a specific data item or control point inside a service.

Examples:
- temperature value
- humidity value
- LED command
- device status

### Descriptor
A **descriptor** provides metadata or configuration associated with a characteristic.

### Properties
A characteristic can have one or more properties such as:

- **Read**: central reads the value
- **Write**: central writes a new value
- **Notify**: peripheral sends updates to a subscribed central

### Simple mental model
- **Service** = folder
- **Characteristic** = file
- **Property** = allowed action on that file

### Example
**Custom Sensor Service**
- Device Status Characteristic → Read
- LED Control Characteristic → Write
- Temperature Characteristic → Read, Notify

---

## 9. ESP32-C6 BLE Architecture at Application Level

At the application level, a BLE peripheral on ESP32-C6 usually includes:

1. BLE stack initialization
2. Device name setup
3. Advertising configuration
4. Service definition
5. Characteristic definition
6. Event handling for connect, read, write, and disconnect

### What students should recognize in the code

- where advertising starts
- where the service is declared
- where the characteristic is declared
- where value access is handled

---

## 10. Class Plan (2 Hours)

| Time | Topic | Goal | Activity |
|---|---:|---|---|
| 0–10 min | Opening and context | Connect BLE to familiar devices | Guided discussion |
| 10–25 min | Bluetooth Classic vs BLE | Build conceptual distinction | Comparison table + examples |
| 25–40 min | Central and peripheral roles | Identify communication actors | Classification exercise |
| 40–60 min | GATT: services and characteristics | Understand BLE data model | Board examples |
| 60–70 min | ESP32-C6 architecture | Connect theory to implementation | Code walkthrough |
| 70–100 min | Lab: first BLE peripheral | Verify a working BLE node | Flash + scan + read |
| 100–110 min | Evidence capture | Document results | Screenshots + notes |
| 110–120 min | Closure | Synthesize key ideas | Reflection questions |

---

## 11. Hands-On Lab — First BLE Peripheral

### Lab Objective
Create and verify an ESP32-C6 BLE peripheral that:

- advertises a device name
- exposes one BLE service
- exposes one readable characteristic
- can be discovered from a phone or PC scanner

### Tools
- ESP32-C6 DevKit
- VS Code + ESP-IDF
- Serial monitor
- BLE scanner app or desktop BLE tool

### Base Path
Students use a prepared BLE example and focus on:

- build
- flash
- scan
- connect
- read the characteristic
- document evidence

### Advanced Extension
Students modify:

- device name
- characteristic value
- add one writable characteristic for LED control

---

## 12. Lab Procedure

1. Open the provided ESP-IDF BLE project.
2. Identify the following elements in the source code:
   - device name
   - service UUID
   - characteristic UUID
   - characteristic property
3. Build and flash the firmware to the ESP32-C6.
4. Open the serial monitor.
5. Verify that BLE initialization completed correctly.
6. Open the BLE scanner app on a phone or PC.
7. Search for the BLE device.
8. Confirm the advertised name is visible.
9. Connect to the peripheral.
10. Inspect the available services and characteristics.
11. Read the characteristic value.
12. Save the required evidence in the technical log.

---

## 13. Verification Checkpoints

Students must verify all of the following:

- the board boots correctly
- BLE advertising starts successfully
- the advertised name matches the expected name
- the service is visible in the scanner
- the characteristic is readable
- the student can correctly identify which device is central and which is peripheral

---

## 14. Evidence Required for the Technical Log

Include the following:

1. Screenshot of the BLE scanner showing the device advertisement
2. Screenshot showing the service and characteristic
3. Serial log showing successful startup
4. Short explanation of:
   - central vs peripheral
   - service vs characteristic
   - one practical use case for BLE in an embedded product

---

## 15. In-Class Discussion Activity

### Prompt
A battery-powered temperature sensor must be configured locally from a smartphone and periodically share measurements with a nearby device.

### Questions
1. Which device acts as the BLE peripheral?
2. Which device acts as the BLE central?
3. Why is BLE a good fit for this application?
4. Which characteristic property would be useful if the sensor value changes frequently?
5. What is the difference between discovering the device and reading a value from it?

### Expected reasoning
- sensor node = peripheral
- smartphone = central
- BLE provides short-range, low-power interaction
- **Notify** is useful for frequent updates
- discovery happens during advertising/scanning; reading occurs after connection through GATT

---

## 16. Teaching Notes and Common Misconceptions

### Misconception 1
**“BLE is just another serial link.”**

Correction: BLE usually exposes structured data through services and characteristics.

### Misconception 2
**“Advertising means the device is already connected.”**

Correction: advertising is only discovery; connection is a separate stage.

### Misconception 3
**“Every BLE device behaves the same way.”**

Correction: behavior depends on the GATT design, roles, and characteristic properties.

### Misconception 4
**“BLE is always the best wireless option because it uses less power.”**

Correction: BLE is excellent for local low-power interaction, but it is not ideal for every architecture or range requirement.

---

## 17. Example Teaching Skeleton (Conceptual ESP-IDF)

```c
/*
 * BLE Peripheral Skeleton for ESP32-C6
 * Conceptual example for instructional use.
 *
 * Safety note:
 * Do not power external modules directly from GPIO pins.
 * Verify the board supply and USB connection before testing.
 */

#include <stdio.h>
#include "esp_log.h"

static const char *TAG = "BLE_CLASS";

void app_main(void)
{
    ESP_LOGI(TAG, "Initializing BLE stack...");

    // 1. Initialize BLE controller and stack
    // 2. Register GAP callback
    // 3. Register GATT server callback
    // 4. Define service UUID
    // 5. Define characteristic UUID and properties
    // 6. Start service
    // 7. Configure advertising payload
    // 8. Start advertising

    ESP_LOGI(TAG, "BLE advertising started.");
}
```

---

## 18. Suggested Slide Flow

1. What BLE is
2. Bluetooth Classic vs BLE
3. Central and peripheral roles
4. Advertising, scanning, and connecting
5. GATT: services and characteristics
6. ESP32-C6 BLE application blocks
7. Lab procedure
8. Evidence required
9. Common misconceptions
10. Reflection and closure

---

## 19. Homework

### Base Assignment
Add a section to the technical log including:

- summary of BLE roles
- screenshot of discovered BLE device
- explanation of one service and one characteristic
- short reflection: **Where would BLE be useful in an embedded system?**

### Advanced Assignment
Modify the example so the characteristic value changes over time and verify the updated value from the scanner.

---

## 20. Mini Rubric for This Session

| Criterion | Excellent | Satisfactory | Needs Improvement |
|---|---|---|---|
| BLE role identification | Correctly identifies all roles and explains them | Minor confusion in one case | Cannot distinguish central and peripheral |
| GATT understanding | Correctly explains service, characteristic, and properties | Explains most elements with minor errors | Confuses structure or purpose |
| Practical implementation | Device advertises and characteristic is readable | Device advertises but read verification is incomplete | Firmware does not function or cannot be verified |
| Technical log evidence | Complete screenshots and concise explanation | Missing one evidence item | Weak or incomplete documentation |

---

## 21. Bill of Materials (Estimated MXN)

| Item | Qty | Approx. Unit Cost (MXN) | Approx. Total (MXN) |
|---|---:|---:|---:|
| ESP32-C6 DevKit | 1 | 180–280 | 180–280 |
| USB cable | 1 | 60–100 | 60–100 |
| Breadboard | 1 | 70–120 | 70–120 |
| Jumper wires | 1 set | 50–80 | 50–80 |
| Smartphone with BLE scanner app | 1 | Existing | 0 |
| PC with VS Code + ESP-IDF | 1 | Institutional | 0 |

**Estimated practice total per station:** **360–580 MXN**

---

## 22. Base Path and Advanced Extensions

### Base Path
- understand BLE roles
- flash prepared BLE peripheral example
- verify advertising
- read one characteristic
- document evidence

### Advanced Extensions
- add writable characteristic
- toggle LED from phone app
- add notify characteristic
- expose sensor data as GATT values
- design a richer BLE interface with multiple characteristics

---

## 23. Closing Reflection Questions

1. What problem does BLE solve well in nearby device interaction?
2. Why is GATT more structured than sending raw serial data?
3. What is the practical difference between advertising and connecting?
4. What trade-offs exist between convenience, power consumption, and communication range?

---

## Verification and Risks

### Technical assumptions
- ESP32-C6 BLE examples and toolchain are functioning correctly.
- Students already know how to compile, flash, and use the serial monitor.
- At least one BLE-capable phone or PC is available per team.

### Potential hardware and software risks
- **ESP32-C6 availability:** keep spare kits available in case of damaged boards.
- **Driver or toolchain issues:** validate each workstation before class.
- **Phone app variability:** provide one recommended scanner app and reference screenshots.
- **BLE example complexity:** start from a prepared template to reduce setup overhead.

### Pedagogical risks
- Students may confuse Bluetooth Classic and BLE.
  - **Mitigation:** emphasize the comparison table early.
- Students may confuse advertising with connection.
  - **Mitigation:** repeat the communication flow with concrete examples.
- Students may get lost in stack internals.
  - **Mitigation:** focus on application-level structure rather than low-level implementation details.

