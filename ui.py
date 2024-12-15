import gradio as gr
import encryption , decryption

def combine_midi(option , file1 , file2 , en):
    
    if option == "encrypt":
        encryption.main(file1.name, en)
        return "output.mid", ""

    else:
        midi1 = decryption.main(file1.name, file2.name)
        return None,midi1

iface = gr.Interface(
    fn=combine_midi,
    inputs=[gr.components.Dropdown(choices=["encrypt", "decrypt"], label="選擇模式",default="encrypt"),gr.components.File(type="file", label="First MIDI File"), gr.components.File(type="file", label="Decrypt File"),gr.components.Textbox(label="Encrypt Content")],
    outputs=[gr.components.File(label="Combined MIDI File"),gr.components.Textbox(label="Decrypt Result")]
    ,css="footer{display:none !important}",allow_flagging="never"
)
iface.launch(share=True)
