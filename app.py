import gradio as gr
from sidekick import Sidekick

# Initialize Sidekick instance and run async setup
async def setup():
    sidekick = Sidekick()
    await sidekick.setup()
    return sidekick

# Main message handler: runs Sidekick logic and returns updated chat
async def process_message(sidekick, message, success_criteria, history):
    results = await sidekick.run_superstep(message, success_criteria, history)
    return results, sidekick

# Reset Sidekick state and clear UI inputs
async def reset():
    new_sidekick = Sidekick()
    await new_sidekick.setup()
    return "", "", None, new_sidekick

# Cleanup function to safely release resources on app shutdown
def free_resources(sidekick):
    print("Cleaning up")
    try:
        if sidekick:
            sidekick.cleanup()
    except Exception as e:
        print(f"Exception during cleanup: {e}")

# Build Gradio UI
with gr.Blocks(title="Sidekick", theme=gr.themes.Default(primary_hue="emerald")) as ui:
    gr.Markdown("## Sidekick Personal Co-Worker")
    sidekick = gr.State(delete_callback=free_resources)

    with gr.Row():
        chatbot = gr.Chatbot(label="Sidekick", height=300, type="messages")
    with gr.Group():
        with gr.Row():
            message = gr.Textbox(show_label=False, placeholder="Your request to the Sidekick")
        with gr.Row():
            success_criteria = gr.Textbox(
                show_label=False, placeholder="What are your success critiera?"
            )
    with gr.Row():
        reset_button = gr.Button("Reset", variant="stop")
        go_button = gr.Button("Go!", variant="primary")

    # Load Sidekick when UI starts
    ui.load(setup, [], [sidekick])
    # Submit on message enter
    message.submit(
        process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick]
    )
    # Submit on success criteria enter
    success_criteria.submit(
        process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick]
    )
    # Submit on button click
    go_button.click(
        process_message, [sidekick, message, success_criteria, chatbot], [chatbot, sidekick]
    )
    # Reset UI + state
    reset_button.click(reset, [], [message, success_criteria, chatbot, sidekick])

# Launch app in browser
ui.launch(inbrowser=True)
