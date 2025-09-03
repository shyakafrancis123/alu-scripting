#!/usr/bin/env ruby

# Extract sender, receiver, and flags from TextMe SMS log
log_line = ARGV[0]

# Regular expression to match the log format
# Looking for [from:SENDER] [to:RECEIVER] [flags:FLAGS]
regex = /\[from:([^\]]+)\] \[to:([^\]]+)\] \[flags:([^\]]+)\]/

match = log_line.match(regex)

if match
  sender = match[1]
  receiver = match[2]  
  flags = match[3]
  
  puts "#{sender},#{receiver},#{flags}"
end
