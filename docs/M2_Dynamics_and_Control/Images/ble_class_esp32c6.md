# Bluetooth Low Energy Foundations with ESP32-C6

## Executive Summary
This session introduces **Bluetooth Low Energy (BLE)** as a short-range, low-power wireless protocol for embedded systems using the **ESP32-C6**. Since students already studied **MQTT over Wi-Fi**, this class emphasizes the contrast between **internet-oriented publish/subscribe communication** and **local proximity-based BLE communication**. Students will learn BLE roles, the discovery process, and the **GATT model** of services and characteristics. The practical activity focuses on implementing and verifying a basic BLE peripheral on the ESP32-C6. By the end of the session, students will be able to explain when BLE is preferable to Wi-Fi/MQTT and verify a working BLE peripheral using a scanner tool.

---

## 1. Session Information

- **Session title:** Bluetooth Low Energy Foundations with ESP32-C6
- **Duration:** 2 hours
- **Format:** Face-to-face, instructor-led, with lab activity
- **Course stage:** After Wi-Fi + HTTP + MQTT, before Zigbee/Thread/Matter
- **Prerequisites:**
  - C/C++ programming
  - Basic ESP32 project structure
  - GPIO and timers
  - Serial debugging
  - Basic networking concepts
  - Prior experience with Wi-Fi and MQTT on ESP32-C6

---

## 2. SMART Learning Outcomes

By the end of this session, students will be able to:

1. **Differentiate** BLE and Wi-Fi/MQTT by identifying at least **three technical differences** in range, topology, and energy consumption.
2. **Identify** the BLE roles of **central** and **peripheral**, and correctly classify at least **4 of 5 example devices**.
3. **Interpret** a simple BLE GATT structure by mapping the relationship among **service, characteristic, and properties**.
4. **Configure and run** an ESP32-C6 BLE peripheral that advertises its presence and exposes **one readable characteristic**.
5. **Verify** BLE operation using a scanner tool and document evidence in the technical log.

---

## 3. Why BLE After MQTT?

Students have already implemented **MQTT over Wi-Fi**, which is useful for:

- communication through an IP network
- broker-based publish/subscribe architectures
- telemetry and command exchange across a LAN or Internet-connected system
- multi-device data aggregation

BLE addresses a different design space:

- short-range local connectivity
- lower power operation
- direct interaction with nearby devices such as smartphones
- fast provisioning, local control, and sensor exposure without requiring Wi-Fi credentials or an MQTT broker

### Key instructional contrast

| Topic | Wi-Fi + MQTT | BLE |
|---|---|---|
| Typical range | Higher | Short-range |
| Infrastructure | Requires AP/network and usually broker | Can work locally without router |
| Communication style | Publish/subscribe via broker | Advertising + GATT-based interaction |
| Power consumption | Higher | Lower |
| Good for | Cloud/LAN telemetry, gateways, dashboards | Local sensors, provisioning, phone interaction |
| Typical client tool | MQTT Explorer, broker, dashboards | BLE scanner app, phone, BLE central |

### Design question for students
**If the user is standing next to the device with a phone, do we really need Wi-Fi + broker for the first interaction?**

This question motivates BLE as a practical local interface.

---

## 4. Core BLE Concepts

### 4.1 What is BLE?
**Bluetooth Low Energy (BLE)** is a wireless communication technology optimized for **small data exchanges**, **short range**, and **low power consumption**.

It is commonly used in:

- wearables
- wireless sensors
- beacons
- medical devices
- local device configuration
- battery-powered embedded nodes

### 4.2 BLE is not “MQTT without Wi-Fi”
BLE does not use topics, brokers, or IP packets in the same way as MQTT.

Instead, BLE is structured around:

- **advertising**: announcing presence
- **scanning**: searching for nearby devices
- **connections**: optional direct links
- **GATT attributes**: structured data items exposed by the peripheral

---

## 5. BLE Roles

### Peripheral
A **peripheral** is typically the embedded device that:

- advertises its presence
- exposes data or functions
- waits for a central device to connect

Examples:

- smart temperature sensor
- fitness monitor
- industrial beacon
- ESP32-C6 sensor node

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

## 6. BLE Communication Flow

A simplified BLE interaction usually follows this sequence:

1. The peripheral starts **advertising**.
2. The central starts **scanning**.
3. The central detects the advertiser.
4. The central optionally **connects**.
5. The central reads, writes, or subscribes to characteristics.

### Important distinction
- **Advertising** is discovery.
- **Connection** is deeper interaction.
- A device may be discoverable even before any connection exists.

---

## 7. GATT Model

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
- **Notify**: peripheral pushes updates to subscribed central

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

## 8. BLE vs MQTT: Engineering Perspective

Students already know this MQTT pattern:

- device joins Wi-Fi
- device connects to broker
- publishes telemetry to a topic
- receives commands from a command topic

BLE is different:

- no Wi-Fi association required
- no broker required
- interaction is local and direct
- data is exposed through characteristics rather than topic namespaces

### Practical comparison

| Engineering need | Better fit |
|---|---|
| Send data to dashboard or cloud through network | MQTT over Wi-Fi |
| Configure a nearby device from a phone | BLE |
| Battery-powered short-range wearable sensor | BLE |
| Multi-room telemetry architecture | MQTT over Wi-Fi |
| Device commissioning before Wi-Fi credentials are available | BLE |

### Design insight
BLE and MQTT are **not competitors in all cases**. In modern embedded systems, they are often **complementary**.

Example:
- BLE for provisioning or local service
- Wi-Fi + MQTT for remote telemetry and fleet integration

---

## 9. ESP32-C6 BLE Architecture (Practical Level)

At the application level, a BLE peripheral on ESP32-C6 usually includes:

1. BLE stack initialization
2. Device name setup
3. Advertising configuration
4. Service definition
5. Characteristic definition
6. Event handling for connect/read/write/disconnect

### What students need to understand today
They do **not** need full stack internals yet.

They do need to identify:

- where advertising starts
- where the service is declared
- where the characteristic is declared
- where value access is handled

---

## 10. Class Plan (2 Hours)

| Time | Topic | Goal | Activity |
|---|---:|---|---|
| 0–10 min | Opening and context | Connect BLE to familiar devices | Guided discussion |
| 10–25 min | BLE vs Wi-Fi/MQTT | Build conceptual contrast | Comparison table + examples |
| 25–40 min | Roles: central and peripheral | Identify communication actors | Classification exercise |
| 40–60 min | GATT: services and characteristics | Understand BLE data model | Board examples |
| 60–70 min | ESP32-C6 architecture | Connect theory to implementation | Code walkthrough |
| 70–100 min | Lab: first BLE peripheral | Verify a working BLE node | Flash + scan + read |
| 100–110 min | Evidence capture | Document results | Screenshots + notes |
| 110–120 min | Closure | Synthesize BLE vs MQTT usage | Reflection questions |

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
   - one reason BLE is preferable to MQTT/Wi-Fi in this use case

---

## 15. In-Class Discussion Activity

### Prompt
A battery-powered temperature sensor must be configured locally from a smartphone and later may report telemetry to a remote dashboard.

### Questions
1. Which protocol is more appropriate for the initial local setup: BLE or MQTT?
2. Which protocol is more appropriate for remote monitoring: BLE or MQTT?
3. Could both be used in the same product?
4. What role would the smartphone take in BLE?
5. What role would the sensor node take in BLE?

### Expected reasoning
- BLE is better for local setup and direct nearby interaction.
- MQTT is better for network-based telemetry and integration.
- Both can coexist in a single device architecture.
- smartphone = central
- sensor node = peripheral

---

## 16. Teaching Notes and Common Misconceptions

### Misconception 1
**“BLE is just another serial link.”**

Correction: BLE usually exposes structured data through services and characteristics.

### Misconception 2
**“BLE replaces MQTT.”**

Correction: BLE and MQTT solve different communication problems and often complement each other.

### Misconception 3
**“If the device advertises, it is already connected.”**

Correction: advertising is only discovery; connection is a separate stage.

### Misconception 4
**“BLE is always the best wireless option because it uses less power.”**

Correction: BLE is excellent for local low-power interaction, but it is not ideal for every architecture, especially remote network telemetry.

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
2. Why BLE if we already have MQTT?
3. BLE vs Wi-Fi/MQTT comparison
4. Central and peripheral roles
5. Advertising, scanning, connecting
6. GATT: services and characteristics
7. ESP32-C6 BLE application blocks
8. Lab procedure
9. Evidence required
10. Reflection: when to choose BLE, MQTT, or both

---

## 19. Homework

### Base Assignment
Add a section to the technical log including:

- BLE vs MQTT comparison
- screenshot of discovered BLE device
- explanation of one service and one characteristic
- short reflection: **When would I choose BLE instead of MQTT in an embedded system?**

### Advanced Assignment
Modify the example so the characteristic value changes over time and verify the updated value from the scanner.

---

## 20. Mini Rubric for This Session

| Criterion | Excellent | Satisfactory | Needs Improvement |
|---|---|---|---|
| BLE role identification | Correctly identifies all roles and explains them | Minor confusion in one case | Cannot distinguish central and peripheral |
| GATT understanding | Correctly explains service, characteristic, and properties | Explains most elements with minor errors | Confuses structure or purpose |
| Practical implementation | Device advertises and characteristic is readable | Device advertises but read verification is incomplete | Firmware does not function or cannot be verified |
| Comparison with MQTT | Clearly explains when BLE or MQTT is preferable | General contrast is present but incomplete | Cannot justify protocol choice |
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
- compare BLE with previously studied MQTT workflow

### Advanced Extensions
- add writable characteristic
- toggle LED from phone app
- add notify characteristic
- expose sensor data as GATT values
- design a dual-interface architecture: BLE for local provisioning + MQTT for remote telemetry

---

## 23. Closing Reflection Questions

1. What problem does BLE solve better than MQTT in a nearby device interaction?
2. Why is GATT more structured than sending raw serial data?
3. Why might a real embedded product use both BLE and MQTT?
4. What are the trade-offs between convenience, power consumption, and infrastructure?

---

## Verification and Risks

### Technical assumptions
- ESP32-C6 BLE examples and toolchain are functioning correctly.
- Students already know how to compile, flash, and use the serial monitor.
- At least one BLE-capable phone or PC is available per team.
- Students have already completed the MQTT class and can compare architectures.

### Potential hardware/software risks
- **ESP32-C6 availability:** board stock may be inconsistent; keep spare units available.
- **Driver/toolchain issues:** USB or ESP-IDF setup problems may consume lab time; validate stations before class.
- **Scanner tool variability:** BLE scanner apps differ in interface; standardize one recommended app if possible.
- **Example complexity:** a full BLE server can be dense for a first exposure; provide a prepared baseline project.

### Pedagogical risks
- Students may confuse BLE with Bluetooth Classic.
  - **Mitigation:** present a clear comparison early.
- Students may assume BLE works like MQTT topics.
  - **Mitigation:** explicitly contrast topic-based messaging with GATT.
- Students may focus on API details instead of the communication model.
  - **Mitigation:** keep the first session architecture-level and verification-focused.

### Missing prerequisite risks
- Weak understanding of client/server or requester/responder roles.
  - **Mitigation:** connect BLE central/peripheral roles to familiar interaction patterns.
- Weak debugging discipline.
  - **Mitigation:** require both serial evidence and scanner evidence in the lab log.
