{
  "targets": [
    {
      "target_name": "SQLParser",
      "sources": ["SQLParser.cc"],
      "cflags_cc!": ["-fno-rtti"],
      "cflags_cc+": ["-DBOOST_NO_EXCEPTIONS"]
    }
  ]
}
