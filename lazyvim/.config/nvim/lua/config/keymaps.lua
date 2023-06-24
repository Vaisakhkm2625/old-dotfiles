-- Keymaps are automatically loaded on the VeryLazy event
-- Default keymaps that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/keymaps.lua
-- Add any additional keymaps here

-- nvim-tmux-navigation keymaps
local nvim_tmux_nav = require("nvim-tmux-navigation")
local wk = require("which-key")

vim.keymap.set("n", "<C-h>", nvim_tmux_nav.NvimTmuxNavigateLeft)
vim.keymap.set("n", "<C-j>", nvim_tmux_nav.NvimTmuxNavigateDown)
vim.keymap.set("n", "<C-k>", nvim_tmux_nav.NvimTmuxNavigateUp)
vim.keymap.set("n", "<C-l>", nvim_tmux_nav.NvimTmuxNavigateRight)
vim.keymap.set("n", "<C-\\>", nvim_tmux_nav.NvimTmuxNavigateLastActive)
vim.keymap.set("n", "<C-Space>", nvim_tmux_nav.NvimTmuxNavigateNext)

wk.register({ ["<leader>L"] = { name = "+LazyVim" } })
vim.keymap.set("n", "<leader>La", "<cmd>Alpha<cr>", { desc = "Alpha" })
vim.keymap.set("n", "<leader>Lc", "<cmd>:e $MYVIMRC<cr>", { desc = "Config" })

wk.register({ ["<leader>h"] = { name = "+Quick" } })
vim.keymap.set("n", "<leader>sn", "<cmd>Telescope notify<cr>", { desc = "Notification history" })
vim.keymap.set("n", "<leader>hh", "<cmd>source %<cr>", { desc = "Source current file" })

-- tmp
vim.keymap.set(
  "n",
  "<leader>hy",
  "<cmd>lua require('hologram-math-preview').update_under_cursor()<cr>",
  { desc = "hologram-math-preview update_under_cursor" }
)
