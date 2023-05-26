-- Autocmds are automatically loaded on the VeryLazy event
-- Default autocmds that are always set: https://github.com/LazyVim/LazyVim/blob/main/lua/lazyvim/config/autocmds.lua
-- Add any additional autocmds here

-- create autocmd group
local function augroup(name)
  return vim.api.nvim_create_augroup("myautocmds_" .. name, { clear = true })
end

-- Don't auto commenting new lines
vim.api.nvim_create_autocmd("BufEnter", {
  group = augroup("remove_auto_cmds"),
  pattern = "",
  callback = function()
    vim.opt.formatoptions:remove({ "c", "r", "o" })
  end,
})
