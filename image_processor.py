# image_processor.py
from flask import Flask, request, jsonify
from skimage import io, filters
import os

app = Flask(__name__)


@app.route('/SEGMENT', methods=['POST'])
def segment_image():

    data = request.json
    input_path = data.get('input_path')

    print(f"input path: {input_path}")

    if not input_path or not os.path.exists(input_path):
        return (
            jsonify({'error': 'Input path is invalid or does not exist'}),
            400,
        )

    try:
        # Read the image
        image = io.imread(input_path)

        # Apply Gaussian filter
        filtered_image = filters.gaussian(image, sigma=1)

        # Save the filtered image
        output_path = os.path.splitext(input_path)[0] + '_filtered.tiff'
        io.imsave(output_path, (filtered_image * 255).astype('uint8'))

        return (
            jsonify(
                {
                    'message': 'Image processed successfully',
                    'output_path': output_path,
                }
            ),
            200,
        )
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5025)
