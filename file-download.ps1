$invocation = (Get-Variable MyInvocation).Value
$directory =  Split-Path $invocation.MyCommand.Path
$urls = 'http://www.textfiles.com/etext/FICTION/2city10.txt',
        'http://www.textfiles.com/etext/FICTION/anna_karenina',
        'http://www.textfiles.com/etext/FICTION/2000010.txt',
        'http://www.textfiles.com/etext/FICTION/center_earth',
        'http://www.textfiles.com/etext/FICTION/moon10a.txt'


foreach ($url in $urls) {
    $paths = $url.Split("/")
    $file = $paths[$paths.Length - 1]
    if (-not $file.Contains(".txt")){
        $file = $file + ".txt"  
    }
    $ProgressPreference = 'SilentlyContinue'   
    wget $url -OutFile ($directory + "\Input_Texts\" + $file)
}

python .\encrypt.py > ($directory + "\output.txt")

$file_data = Get-Content -Path ($directory + "\output.txt")

foreach ($file in $file_data) {
    $file = $file.Trim()
}

$original = (Get-Content ($directory + "\Input_Texts\" + $file_data[0])).ToLower()
$decrypted = (Get-Content ($directory + "\" + $file_data[1])).ToLower()

$ret = Compare-Object $original $decrypted