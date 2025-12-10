from PIL import Image
import os


def extract_mosaic_tiles(
    input_texture_path: str,
    out_path: str = "data/mosaics",
    tile_size: int = 48,
    grid_w: int = 45,
    grid_h: int = 45,
    prefix: str = "face",
    ext: str = ".png",
):
    """
    Extracts tiled sub-images from a grid-based mosaic texture and saves them to disk.

    Args:
        input_texture_path: Path to the sprite sheet image.
        out_path: Directory to save extracted tiles.
        tile_size: Width/height of each tile in pixels.
        grid_w: Number of columns in the grid.
        grid_h: Number of rows in the grid.
        prefix: Filename prefix for saved tiles.
        ext: File extension for output images.
    """

    os.makedirs(out_path, exist_ok=True)

    img = Image.open(input_texture_path)
    img_w, img_h = img.size

    expected_w = grid_w * tile_size
    expected_h = grid_h * tile_size

    # Safety check
    if img_w < expected_w or img_h < expected_h:
        raise ValueError(
            f"Image too small: got {img_w}x{img_h}, "
            f"expected at least {expected_w}x{expected_h}"
        )

    count = 0
    for row in range(grid_h):
        for col in range(grid_w):
            left = col * tile_size
            top = row * tile_size
            right = left + tile_size
            bottom = top + tile_size

            tile = img.crop((left, top, right, bottom))

            filename = f"{prefix}_{row:03d}_{col:03d}{ext}"
            tile_path = os.path.join(out_path, filename)

            tile.save(tile_path)
            count += 1

    return count


def main():
    num_tiles = extract_mosaic_tiles(
        "data/mosaic_texture/25745_avatars.png"
    )

    print(f"Extracted {num_tiles} tiles!")


if __name__ == "__main__":
    main()