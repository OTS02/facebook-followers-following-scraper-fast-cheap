# Facebook Followers & Following Scraper

> A powerful scraper that extracts detailed follower and following data from Facebook profiles and pages.
> This tool is built to deliver fast, structured, and actionable data for analytics, research, and audience insights.
> Ideal for marketers, researchers, and businesses needing reliable Facebook follower data at scale.


<p align="center">
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://github.com/za2122/footer-section/blob/main/media/scraper.png" alt="Bitbash Banner" width="100%"></a>
</p>
<p align="center">
  <a href="https://t.me/devpilot1" target="_blank">
    <img src="https://img.shields.io/badge/Chat%20on-Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Telegram">
  </a>&nbsp;
  <a href="https://wa.me/923249868488?text=Hi%20BitBash%2C%20I'm%20interested%20in%20automation." target="_blank">
    <img src="https://img.shields.io/badge/Chat-WhatsApp-25D366?style=for-the-badge&logo=whatsapp&logoColor=white" alt="WhatsApp">
  </a>&nbsp;
  <a href="mailto:sale@bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Email-sale@bitbash.dev-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Gmail">
  </a>&nbsp;
  <a href="https://bitbash.dev" target="_blank">
    <img src="https://img.shields.io/badge/Visit-Website-007BFF?style=for-the-badge&logo=google-chrome&logoColor=white" alt="Website">
  </a>
</p>




<p align="center" style="font-weight:600; margin-top:8px; margin-bottom:8px;">
  Created by Bitbash, built to showcase our approach to Scraping and Automation!<br>
  If you are looking for <strong>Facebook Followers & Following Scraper 📊👥 - Fast & cheap 💬⭐</strong> you've just found your team — Let’s Chat. 👆👆
</p>


## Introduction

This project retrieves structured information about followers and following lists from any accessible Facebook profile or page.
It solves the challenge of manually collecting audience data by automating discovery, extraction, and formatting.
It is designed for analysts, growth experts, researchers, and developers who require accurate social data for insights or automation.

### Why Use a Facebook Followers & Following Scraper?

- Extract follower and following lists at scale with minimal effort.
- Access valuable profile details such as gender, location, and profile metadata.
- Gather insights for marketing, competitor tracking, and audience segmentation.
- Retrieve structured outputs ready for analytics pipelines.
- Handle public and authentication-required profiles where permitted.

## Features

| Feature | Description |
|--------|-------------|
| Fast follower extraction | Quickly gathers followers and following lists from pages and profiles. |
| Detailed profile metadata | Retrieves ID, name, URL, gender, image, and more. |
| Supports large-scale scraping | Allows defining maximum result limits for bulk extraction. |
| Works with profiles requiring access | Extracts data where login is required when permitted. |
| Multi-format export | Output data can be saved as JSON, CSV, XML, Excel, or HTML. |

---

## What Data This Scraper Extracts

| Field Name | Field Description |
|------------|------------------|
| id | Unique Facebook-generated profile identifier. |
| name | Full display name of the follower/following profile. |
| image_uri | Direct URL to the user’s profile picture. |
| profile_url | URL of the Facebook profile page. |
| subtitle_text | Additional profile info, such as location or description. |
| gender | Detected or listed gender. |
| friendship_status | Interaction capability (e.g., CAN_REQUEST). |
| short_name | Shortened display name or nickname. |

---

## Example Output


    {
        "id": "YXBwX2l0ZW06MTAwMDAzNTAwODY1ODgyOjIzNTYzMTgzNDk6MzM6OjEwMDAxMDcwNDA0NjAwOQ==",
        "name": "Alex Proyas",
        "image_uri": "https://scontent.frba3-1.fna.fbcdn.net/v/t39.30808-1/454952264_2238778823155564_5874290976386990675_n.jpg",
        "profile_url": "https://www.facebook.com/RealAlexProyas",
        "subtitle_text": "Sydney, Australia",
        "gender": "MALE",
        "friendship_status": "CAN_REQUEST",
        "short_name": "Alex"
    }

---

## Directory Structure Tree


    Facebook Followers & Following Scraper 📊👥 - Fast & cheap 💬⭐/
    ├── src/
    │   ├── runner.py
    │   ├── extractors/
    │   │   ├── facebook_parser.py
    │   │   └── utils_time.py
    │   ├── outputs/
    │   │   └── exporters.py
    │   └── config/
    │       └── settings.example.json
    ├── data/
    │   ├── inputs.sample.txt
    │   └── sample.json
    ├── requirements.txt
    └── README.md

---

## Use Cases

- **Marketing analysts** use it to map audience demographics so they can optimize targeting and messaging.
- **Researchers** gather large datasets of follower relationships to study social behavior and trends.
- **Businesses** monitor competitor followers to identify potential leads and engagement opportunities.
- **Community managers** track audience growth to improve engagement strategies.
- **Data engineers** integrate structured follower data into analytics workflows for automated reporting.

---

## FAQs

**Does this scraper work on both profiles and pages?**
Yes, it supports both Facebook profiles and pages, retrieving followers or following lists where visible.

**Is authentication required?**
Some profiles require login access. When access is allowed, the scraper can retrieve data accordingly.

**What limits should I set when scraping?**
You may specify a maximum number of results to control dataset size and performance.

**What export formats are supported?**
Extracted data can be exported to JSON, CSV, XML, Excel, or HTML for flexible downstream use.

---

## Performance Benchmarks and Results

**Primary Metric:** Average extraction speed of several hundred profiles per minute under optimal conditions.
**Reliability Metric:** Consistent success rate above 95% when accessing publicly available or permitted data.
**Efficiency Metric:** Low resource consumption due to lightweight parsing and batching techniques.
**Quality Metric:** High data completeness with over 90% of profiles returning full metadata fields when available.


<p align="center">
<a href="https://calendar.app.google/74kEaAQ5LWbM8CQNA" target="_blank">
  <img src="https://img.shields.io/badge/Book%20a%20Call%20with%20Us-34A853?style=for-the-badge&logo=googlecalendar&logoColor=white" alt="Book a Call">
</a>
  <a href="https://www.youtube.com/@bitbash-demos/videos" target="_blank">
    <img src="https://img.shields.io/badge/🎥%20Watch%20demos%20-FF0000?style=for-the-badge&logo=youtube&logoColor=white" alt="Watch on YouTube">
  </a>
</p>
<table>
  <tr>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/MLkvGB8ZZIk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review1.gif" alt="Review 1" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash is a top-tier automation partner, innovative, reliable, and dedicated to delivering real results every time.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Nathan Pennington
        <br><span style="color:#888;">Marketer</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtu.be/8-tw8Omw9qk" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review2.gif" alt="Review 2" width="100%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Bitbash delivers outstanding quality, speed, and professionalism, truly a team you can rely on.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Eliza
        <br><span style="color:#888;">SEO Affiliate Expert</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
    <td align="center" width="33%" style="padding:10px;">
      <a href="https://youtube.com/shorts/6AwB5omXrIM" target="_blank">
        <img src="https://github.com/za2122/footer-section/blob/main/media/review3.gif" alt="Review 3" width="35%" style="border-radius:12px; box-shadow:0 4px 10px rgba(0,0,0,0.1);">
      </a>
      <p style="font-size:14px; line-height:1.5; color:#444; margin:0 15px;">
        “Exceptional results, clear communication, and flawless delivery. Bitbash nailed it.”
      </p>
      <p style="margin:10px 0 0; font-weight:600;">Syed
        <br><span style="color:#888;">Digital Strategist</span>
        <br><span style="color:#f5a623;">★★★★★</span>
      </p>
    </td>
  </tr>
</table>
