# BP Tracker - PWA Setup

## PWA Features

This app is configured as a Progressive Web App (PWA) that can be installed on iOS/Android devices.

### Installation on iPhone

1. Open the app URL in Safari
2. Tap the Share button
3. Select **"Add to Home Screen"**
4. The app will appear as a standalone app icon
5. When opened from the home screen, it runs in full-screen mode (no browser UI)

### Required Icons

You need to create two icon files for the PWA:

- `/public/icons/bp-icon-192.png` (192x192 pixels)
- `/public/icons/bp-icon-512.png` (512x512 pixels)

**Icon Design Suggestions:**
- Simple heart or BP monitor icon
- Blue theme (#2563eb) to match the app
- Rounded corners (iOS will add them automatically)
- Transparent background

You can use any image editor or online tool to create these. The icons will be used for:
- Home screen icon on iOS/Android
- App launcher icon
- Splash screen (on some platforms)

### Files Structure

```
apps/QiBP/
├── app.jsx              # Main React component with splash screen
├── index.html           # HTML entry point with PWA meta tags
├── manifest.json        # PWA manifest configuration
├── icons/               # Icon files (create these)
│   ├── bp-icon-192.png
│   └── bp-icon-512.png
└── text.py              # Webhook URL reference
```

**Note:** Icon files should be placed in an `icons/` folder at the root level (or in `public/icons/` if your bundler serves from a public directory). The manifest references them as `/icons/bp-icon-192.png`.

### Splash Screen

The app includes a built-in splash screen that:
- Shows for 1.2 seconds on app launch
- Displays the BP Tracker logo and "Powered by QiAlly"
- Fades out smoothly to the main app

### Notes

- The webhook URL is hard-coded and cannot be changed via settings
- Google Sheet URL can be configured in Settings for dashboard functionality
- All data is sent to Zoho Flow webhook automatically

