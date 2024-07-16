import gradio as gr


def upload_files(files: str | None = None):
    print(f"Tried to upload the following files {files}")

    return files


def create_demo_ui():
    with gr.Blocks(
        title="SP AI assistant for pre-silicon verification",
        theme=gr.themes.Soft(),
    ) as demo:
        with gr.Row():
            with gr.Column(scale=2):
                # with gr.Row():
                # gr.Image(
                #     height=80,
                #     width=100,
                #     min_width=50,
                #     interactive=False,
                #     show_download_button=False,
                #     show_label=False,
                #     value="/mnt/Storage1/grozavu/digital-circuit-chatbot/database/sp_logo.png",
                # )

                # with gr.Column(scale=4):
                gr.Markdown("# SP AI assistant for pre-silicon verification")
                gr.Markdown("### Ask your questions based on the provided knowledge")

                chatbot = gr.Chatbot(
                    height=780,
                    bubble_full_width=False,
                    label="Assistant",
                    show_copy_button=True,
                    layout="bubble",
                    avatar_images=(
                        "/mnt/Storage1/grozavu/digital-circuit-chatbot/database/default-avatar.png",
                        "/mnt/Storage1/grozavu/digital-circuit-chatbot/database/default-avatar.png",
                    ),
                )

                with gr.Row():
                    stop_btn = gr.Button(
                        "Stop",
                        variant="stop",
                        visible=True,
                        scale=1,
                        min_width=150,
                    )
                    clear_button = gr.ClearButton(
                        value="🗑️ Clear", scale=1, min_width=150
                    )

                with gr.Row():
                    text_input = gr.Textbox(
                        lines=1,
                        placeholder="Type question here...",
                        show_label=False,
                        scale=5,
                    )

                    submit_btn = gr.Button(
                        "Submit",
                        variant="primary",
                        scale=1,
                        min_width=150,
                    )

            with gr.Column():
                retrieved_docs = gr.TextArea(
                    label="Retrieved information",
                    interactive=False,
                    value="No data retrieved",
                    max_lines=42,
                )

                # uploaded_files = gr.UploadButton(
                #     file_count="multiple",
                #     file_types=[".pdf"],
                #     label="Upload 📁",
                # )

            clear_button.add([chatbot, text_input, retrieved_docs])
    return (demo, chatbot, text_input, retrieved_docs, submit_btn)


if __name__ == "__main__":
    demo = create_demo_ui()
    demo.queue()
    demo.launch(
        debug=True,
    )
