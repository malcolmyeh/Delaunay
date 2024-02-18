### Delaunay demo
Show triangles (simplices) generated from implementation using Bowyer-Watson's algorithm and SciPy's implementation. 

```bash
usage: python delaunay_demo.py [-h] [-s S]

options:
  -h, --help  show this help message and exit
  -s S        number of points to generate
```

Example:
```bash
python delaunay_demo.py -s 50
```

### Fjallstrom demo
Show interpolated raster that corresponds to TIN resulting from running Fjallstrom's algorithm on input image or generated image. Note: due to inefficiencies in algorithm, running the program on images greater than 30x30 takes a very long time. 

```bash
usage: python fjallstrom_demo.py [-h] [-s S] [-p P] [-e E]

options:
  -h, --help  show this help message and exit
  -s S        side length of raster to generate
  -p P        path to input raster image
  -e E        maximum error for Fjallstrom algorithm
```

Example using input raster:
```bash
python fjallstrom_demo.py -p 15x15.png
```

Example using generated raster:
```bash
python fjallstrom_demo.py -s 15
```

pip install -r requirements.txt
