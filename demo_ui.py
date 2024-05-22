import gradio as gr


RETRIEVED_DATA_PLACEHOLDER = """
['cause the IC to report a fault via the RF E pin. The first is an undervoltage condition of VCC  and the second is if the \nover -current feature has r ecognize d a fault.  Once the fault condition  occurs, the RF E pin is internally pulled to VSS  \nand the fault clear timer is activated. The RF E output stays in the low state until the fault condition has been removed \nand the fault clear timer expires; once the fault clear timer expires, the voltage on the RF E pin will return to its \nexternal pull -up voltage.   \nThe length of the fault clear time pe riod (t FLTCLR ) is determined by exponential charging characteristics of the \ncapacitor where the time constant is set by R RFE and C RFE. Figure 15  shows that R RFE is connected between the external \nsupply (V DD)1) and the RF E pin, while C RFE is placed between the RF E and VSS  pins . \n \n \n \n \n \n \n \n \n \n \n \n \n \nFigure 15  Programming the fault clear timer  \nVCC\nHIN (x3)\nRFE\nITRIP\nVSS COMLIN \nLO HO (x3)VB(x3)\n\n', 'cause the IC to report a fault via the RF E pin. The first is an undervoltage condition of VCC  and the second is if the \nover -current feature has r ecognize d a fault.  Once the fault condition  occurs, the RF E pin is internally pulled to VSS  \nand the fault clear timer is activated. The RF E output stays in the low state until the fault condition has been removed \nand the fault clear timer expires; once the fault clear timer expires, the voltage on the RF E pin will return to its \nexternal pull -up voltage.   \nThe length of the fault clear time pe riod (t FLTCLR ) is determined by exponential charging characteristics of the \ncapacitor where the time constant is set by R RFE and C RFE. Figure 15  shows that R RFE is connected between the external \nsupply (V DD)1) and the RF E pin, while C RFE is placed between the RF E and VSS  pins . \n \n \n \n \n \n \n \n \n \n \n \n \n \nFigure 15  Programming the fault clear timer  \nVCC\nHIN (x3)\nRFE\nITRIP\nVSS COMLIN \nLO HO (x3)VB(x3)\n\n', 'cause the IC to report a fault via the RF E pin. The first is an undervoltage condition of VCC  and the second is if the \nover -current feature has r ecognize d a fault.  Once the fault condition  occurs, the RF E pin is internally pulled to VSS  \nand the fault clear timer is activated. The RF E output stays in the low state until the fault condition has been removed \nand the fault clear timer expires; once the fault clear timer expires, the voltage on the RF E pin will return to its \nexternal pull -up voltage.   \nThe length of the fault clear time pe riod (t FLTCLR ) is determined by exponential charging characteristics of the \ncapacitor where the time constant is set by R RFE and C RFE. Figure 15  shows that R RFE is connected between the external \nsupply (V DD)1) and the RF E pin, while C RFE is placed between the RF E and VSS  pins . \n \n \n \n \n \n \n \n \n \n \n \n \n \nFigure 15  Programming the fault clear timer  \nVCC\nHIN (x3)\nRFE\nITRIP\nVSS COMLIN \nLO HO (x3)VB(x3)\n\n']
""".replace(
    "\n ", ""
)


def get_response(query: str, history: list) -> str:
    response = f"""
    <b>Previous history:</b>
    {str(history)}

    <b>Assistant:</b>

    I don't know the answer to your question:
    {query}
    """

    return response


def upload_files(files: str | None = None):
    print(f"Tried to upload the following files {files}")


def create_demo_ui():
    with gr.Blocks(
        title="AI assistant for pre-silicon verification", theme="Soft"
    ) as demo:
        chatbot = gr.Chatbot(
            render=False,
            height=800,
            # bubble_full_width=False,
            label="IFRO Chatbot",
            show_copy_button=True,
            layout="bubble",
        )

        textbox = gr.Textbox(
            lines=1,
            render=False,
            placeholder="Type question here...",
            show_label=False,
            scale=5,
        )

        clear_button = gr.ClearButton(render=False)

        with gr.Row():
            with gr.Column(scale=2):
                chat_interface = gr.ChatInterface(
                    fn=get_response,
                    theme=gr.themes.Soft(),
                    title="AI assistant for pre-silicon verification",
                    description="<h3>Upload your PDFs and ask questions</h3>",
                    textbox=textbox,
                    chatbot=chatbot,
                    clear_btn=clear_button,
                )

            with gr.Column():
                retrieved_docs = gr.TextArea(
                    label="Retrieved data",
                    interactive=False,
                    value=RETRIEVED_DATA_PLACEHOLDER,
                    max_lines=41,
                )

                files = gr.UploadButton(
                    file_count="multiple",
                    file_types=[".pdf"],
                    label="Upload 📁",
                )

            files.upload(fn=upload_files, inputs=files)
            clear_button.add([chat_interface, retrieved_docs])
    return demo


if __name__ == "__main__":
    demo = create_demo_ui()
    demo.queue()
    demo.launch(debug=True)
