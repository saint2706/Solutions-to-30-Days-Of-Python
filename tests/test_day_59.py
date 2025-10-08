"""Tests for Day 59 generative model helpers."""

from __future__ import annotations

from Day_59_Generative_Models import solutions as day59


def test_autoencoder_reconstruction_loss_decreases() -> None:
    data = day59.generate_swiss_roll(random_state=59)
    log = day59.train_autoencoder_synthetic(data=data, epochs=80)
    assert log.losses[0] > log.losses[-1]
    assert log.losses[0] - log.losses[-1] > 0.05


def test_vae_and_diffusion_losses_drop() -> None:
    data = day59.generate_swiss_roll(random_state=60)
    vae_log = day59.train_variational_autoencoder_synthetic(data=data, epochs=80)
    diffusion_log = day59.train_diffusion_denoiser(data=data, epochs=80)
    assert vae_log.losses[0] - vae_log.losses[-1] > 0.05
    assert diffusion_log.losses[0] - diffusion_log.losses[-1] > 0.05
