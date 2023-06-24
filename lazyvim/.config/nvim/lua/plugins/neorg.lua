return {
  {
    "nvim-neorg/neorg",
    build = ":Neorg sync-parsers",

    keys = {
      { "<leader>nw", "<cmd>Neorg workspace<cr>", desc = "Neorg workspaces" },
      { "<leader>ni", "<cmd>Neorg index<cr>", desc = "Neorg index" },
    },

    opts = {
      load = {
        ["core.defaults"] = {}, -- Loads default behaviour
        ["core.concealer"] = {}, -- Adds pretty icons to your documents
        ["core.summary"] = {},
        ["core.dirman"] = { -- Manages Neorg workspaces
          config = {
            workspaces = {
              notes = "~/notes",
            },
            default_workspace = "notes",
          },
        },
      },
    },
    dependencies = {
      { "nvim-lua/plenary.nvim" },
    },
  },
  {
    "jbyuki/nabla.nvim",
    keys = {
      {
        "<leader>n",
        desc = "Notes",
      },
      {
        "<leader>nl",
        function()
          require("nabla").popup()
        end,
        desc = "Notation",
      },
    },
    config = function()
      require("nabla").enable_virt()
    end,
  },
}

--[[
-- image
--
--

  {
    "jbyuki/nabla.nvim",
    opts = {
      autogen = true, -- auto-regenerate ASCII art when exiting insert mode
      silent = true, -- silents error messages
    },
  },
--
--
clipsub({
    "postfen/clipboard-image.nvim",
    cmd = { "PasteImg" },
    lazy = true,
    config = conf.clipboardimage,
})
norg = {
            img_name = img_func,
            img_dir = "img",
            img_dir_txt = "img",
            affix = "!{%s}[image]",
        },

]]

--[[
--
use({
  "https://git.sr.ht/~whynothugo/lsp_lines.nvim",
  config = function()
    require("lsp_lines").setup()
  end,
})
--
--
--]]
