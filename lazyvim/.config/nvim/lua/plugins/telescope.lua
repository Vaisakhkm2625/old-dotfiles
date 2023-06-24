return {
  "telescope.nvim",
  config = function()
    require("telescope").load_extension("notify")
  end,
  keys = {
    {
      "<leader>t",
      "<cmd>Telescope<cr>",
      desc = "Telescope",
    },
  },
}
