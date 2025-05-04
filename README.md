
# ICS344 Project-03-G07-Final-Project 

This project demonstrates a complete cybersecurity lifecycle from attack to defense, focusing on SSH security vulnerabilities in a controlled environment.

## 🌟 Project Overview

This project explores SSH security through three sequential phases:
1. **Offensive Phase**: Exploiting SSH vulnerabilities using brute-force attacks
2. **Monitoring Phase**: Analyzing attack patterns using SIEM (Splunk)
3. **Defensive Phase**: Implementing countermeasures to prevent SSH attacks

## 🛠️ Environment Setup

- **Victim Machine**: Metasploitable3 (IP: `192.168.0.172`)
- **Attacker Machine**: Kali Linux (IP: `192.168.0.242`)
- **Monitoring**: Splunk SIEM

## 📌 Phase 1: Attacking SSH Service

### Reconnaissance and Attack
- Used Nmap to scan the victim machine and identify the SSH service (port 22)
- Exploited SSH using two methods:
  1. **Metasploit Framework**: Performed credential brute-forcing with `ssh_login` module
  2. **Custom Python Script**: Created a Paramiko-based exploit for automated access

### Key Findings
- Discovered valid credentials: `vagrant:vagrant`
- Successfully gained unauthorized SSH access to the victim machine
- Demonstrated both automated and scripted attack vectors

## 📊 Phase 2: SIEM Analysis with Splunk

### Log Monitoring and Pattern Detection
- Integrated authentication logs from Metasploitable3 into Splunk
- Created visualizations to analyze SSH authentication events
- Identified patterns of attack behavior

### Key Insights
- Detected 341 failed login attempts vs. only 7 successful logins
- Calculated failed-to-success ratio by source IP (ratio ~56 for attacking IP)
- Analyzed SSH session open/close events (96 opens vs. 84 closes)
- Confirmed evidence of brute-force activity from the attacking machine

## 🛡️ Phase 3: Defensive Strategy Implementation

### SSH Hardening Measures
1. **System Updates**: Applied latest security patches
2. **SSH Configuration Changes**:
   - Disabled root login
   - Disabled password authentication
   - Enforced key-based authentication only
3. **Fail2Ban Implementation**:
   - Configured 1-hour ban time
   - Monitored authentication logs in real-time

### Results
- Successfully blocked brute-force attempts
- Confirmed automatic banning of attacking IP addresses
- Verified defense effectiveness by re-running attack

## 🔑 Key Takeaways

1. Default or weak SSH credentials represent a significant security risk
2. Brute-force attacks can be detected through proper log monitoring
3. Simple hardening measures dramatically improve SSH security posture
4. Automated tools like Fail2Ban provide effective dynamic protection

## 🛠️ Work Distribution

- **[AzizHamad03](https://github.com/AzizHamad03)**: Responsible for Phase 1
- **[Basaif-A](https://github.com/Basaif-A)**: Responsible for Phase 2
- **[MoFadel26](https://github.com/MoFadel26)**: Responsible for Phase 3

## 👥 Group Information
- **Section**: ICS344 – Section 3  
- **Group**: #7  
- **Members**:
  - Mohammed Semlali – 202183090  
  - Abedalaziz Hamad – 202183050  
  - Abdulrahman Basaif – 202027940  

---

## 🧠 Ethical Note

> ⚠️ This project was performed in a **legal, isolated environment** using Metasploitable3.  
> All techniques demonstrated are for educational purposes only. Never perform unauthorized access on real systems.

## 📂 Repository Structure

- **Phase 1**: Setup, scanning, and exploitation methods
- **Phase 2**: SIEM analysis and visualization screenshots
- **Phase 3**: Defensive strategy implementation and validation

## 📚 Tools Used

- **Offensive**: Nmap, Metasploit Framework, Python with Paramiko
- **Monitoring**: Splunk Enterprise
- **Defensive**: SSH configuration, Fail2Ban, system hardening


---
