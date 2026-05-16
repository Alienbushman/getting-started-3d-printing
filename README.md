# getting-started-3d-printing

Beginner-friendly 3D printing guides and printable models. Deployed at `alienbushman.com/3d-printing/`.

**Stack:** Astro 5 · Tailwind CSS · static output · nginx

## Local dev

```bash
npm install
npm run dev        # http://localhost:4321/3d-printing/
```

## Build

```bash
npm run build      # output → dist/
```

## Docker

```bash
docker build -t 3d-printing .
docker run --rm -p 8080:80 3d-printing
# open http://localhost:8080/3d-printing/
```

## License

Site code: MIT. Model files retain their original licenses (see each model detail page).
