from moviepy.editor import VideoFileClip

def make_video_lighter(input_file, output_file, target_resolution=(480, 640), bitrate="100k", fps=30):
    """
    Compress and convert a video to .mp4 format with further reduction in size.
    
    :param input_file: Path to the input video file.
    :param output_file: Path to the output .mp4 file.
    :param target_resolution: Target resolution for the output video (height, width).
    :param bitrate: Target bitrate for the output video.
    :param fps: Frames per second for the output video.
    """
    try:
        # Load the video file
        clip = VideoFileClip(input_file)
        
        # Resize the video to the target resolution
        resized_clip = clip.resize(height=target_resolution[0], width=target_resolution[1])
        
        # Write the video to .mp4 format with compression
        resized_clip.write_videofile(
            output_file,
            codec="libx264",
            audio=False,  # Remove audio
            bitrate=bitrate,
            fps=fps,  # Reduce frame rate
        )
        print(f"Lighter video created successfully! Saved as {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    shape = "heart"
    video_type = "shape"

    # Path to the input .mov file
    input_file = f"video_{shape}_{video_type}.MOV"
    # Path to the output .mp4 file
    output_file = f"video_{shape}_{video_type}.mp4"
    
    # Convert, compress, and remove sound
    make_video_lighter(input_file, output_file)
