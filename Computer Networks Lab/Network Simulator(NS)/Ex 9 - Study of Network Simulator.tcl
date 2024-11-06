# Initialize the Simulator
set ns [new Simulator]

# Open Trace and NAM files
set tracefile1 [open out.tr w]
$ns trace-all $tracefile1

set namfile [open out.nam w]
$ns namtrace-all $namfile

# Finish Procedure
proc finish {} {
    global ns tracefile1 namfile
    $ns flush-trace
    close $tracefile1
    close $namfile
    exec nam out.nam &
    exit 0
}

# Define Nodes
set n0 [$ns node]
set n1 [$ns node]
set n2 [$ns node]
set n4 [$ns node]
set n5 [$ns node]

# Define Links
$ns duplex-link $n0 $n2 10Mb 10ms DropTail
$ns queue-limit $n0 $n2 20

# Setup TCP connection
set tcp [new Agent/TCP]
$ns attach-agent $n0 $tcp
set sink [new Agent/TCPSink]
$ns attach-agent $n4 $sink
$ns connect $tcp $sink

# Setup UDP connection
set udp [new Agent/UDP]
$ns attach-agent $n1 $udp
set null [new Agent/Null]
$ns attach-agent $n5 $null
$ns connect $udp $null

# Setup CBR over UDP
set cbr [new Application/Traffic/CBR]
$cbr attach-agent $udp
$cbr set packetsize_ 100
$cbr set rate_ 0.01Mb
$cbr set random_ false

# Run Simulation
$ns at 5.0 "finish"
$ns run
