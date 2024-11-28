# Run the application

```bash
docker build -f dockerfile_imageprocess -t m1srh/image_process:latest .
```

Run the Docker container with the following command:

```bash
docker run -d -p 5025:5025 -v F:/Github/wsireg/input:/app/images m1srh/image_process:latest
```

Replace /path/to/local/images with the path to the directory containing your TIFF images.
