# fsg-canteen-website
# FSG Canteen

**Fried. Steamed. Grilled.**

Multi-page website for FSG Canteen — a street food concept built around three cooking stations arranged in a triangle. Portfolio project.

---

## Pages

| File | Purpose |
|------|---------|
| `index.html` | Landing page — the three stations as primary navigation |
| `menu.html` | Full menu organized by cooking method, with sticky tab switching |
| `about.html` | The concept, the triangle setup, and what FSG actually is |
| `css/style.css` | Shared stylesheet across all three pages |

---

## Images Required

Drop these into an `images/` folder in the root before deploying:

**Landing page**
- `hero.jpg` — main background, full-bleed

**Station cards (index.html)**
- `station-fry.jpg`
- `station-steam.jpg`
- `station-grill.jpg`

**About page**
- `about-hero.jpg`

All images are referenced with `object-fit: cover` and will crop automatically. Landscape orientation works best.

---

## Stack

- HTML / CSS / Vanilla JS — no frameworks, no dependencies
- Google Fonts: Bebas Neue, Barlow Condensed, Barlow
- No build step required

---

## Deployment

### GitHub Pages

1. Push repo to GitHub
2. Go to **Settings → Pages**
3. Set source to **main branch → / (root)**
4. Site goes live at `https://yourusername.github.io/fsg-canteen`

### Netlify

Drag the project folder into [netlify.com/drop](https://netlify.com/drop). Done.

---

## Local Preview

```bash
python3 -m http.server 8080
```

Then open `http://localhost:8080` in your browser. Do not open the HTML files directly — fonts and relative paths need a server to load correctly.

---

## Menu Prices

All prices in `menu.html` are placeholders. Find and update:

| Item | Current Price |
|------|--------------|
| Fried Chicken | $9 |
| Pork Belly Bites | $10 |
| Fries | $4 |
| Onion Rings | $5 |
| Gyoza | $8 |
| Steamed Rice | $3 |
| Steamed Rolls | $4 |
| Beef | $12 |
| Grilled Chicken | $10 |
| Grilled Sausage | $8 |
| Ham + Cheese Sandwich | $9 |
| Corn on the Cob | $4 |

---

## Known Cloudflare Issue

If editing via certain interfaces, Cloudflare may inject a `<script>` tag that truncates JavaScript. If interactivity breaks, check the bottom of the file with:

```bash
tail -10 index.html
```

The file should end cleanly with `</body>` and `</html>`. If it doesn't, restore the complete script block and remove the injected tag.

---

## Project Status

- [x] `index.html` — complete
- [x] `menu.html` — complete
- [x] `about.html` — complete
- [x] `css/style.css` — complete
- [ ] Images — to be added
- [ ] Deploy to GitHub Pages
