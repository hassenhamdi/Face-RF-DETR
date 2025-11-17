from rfdetr import RFDETRMedium

model = RFDETRMedium()

model.train(
    device="cuda",
    dataset_dir='dataset/',
    epochs=10,
    batch_size=4,
    grad_accum_steps=5,
    lr=1e-4,
    output_dir='/output/',
    gradient_checkpointing = True
)
