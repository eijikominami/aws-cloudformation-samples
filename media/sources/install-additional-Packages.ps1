# Copyright Eiji KOMINAMI. All Rights Reserved.

Param()

function Disable-InternetExplorerESC {
    $AdminKey = "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components\{A509B1A7-37EF-4b3f-8CFC-4F3A74704073}"
    $UserKey = "HKLM:\SOFTWARE\Microsoft\Active Setup\Installed Components\{A509B1A8-37EF-4b3f-8CFC-4F3A74704073}"
    Set-ItemProperty -Path $AdminKey -Name "IsInstalled" -Value 0
    Set-ItemProperty -Path $UserKey -Name "IsInstalled" -Value 0
    Write-Host "IE Enhanced Security Configuration (ESC) has been disabled." -ForegroundColor Green
}

function Install-GridDriver {
    $Bucket = "ec2-windows-nvidia-drivers"
    $KeyPrefix = "latest"
    $LocalPath = "$home\Desktop\NVIDIA"
    $Objects = Get-S3Object -BucketName $Bucket -KeyPrefix $KeyPrefix -Region us-east-1
    foreach ($Object in $Objects) {
        $LocalFileName = $Object.Key
        if ($LocalFileName -ne '' -and $Object.Size -ne 0) {
            $LocalFilePath = Join-Path $LocalPath $LocalFileName
            Copy-S3Object -BucketName $Bucket -Key $Object.Key -LocalFile $LocalFilePath -Region us-east-1
        }
    }    
}

try {
    $ErrorActionPreference = "Stop"

    #
    # Settings
    #
    Write-Host "Disable Internet Explorer ESC"
    Disable-InternetExplorerESC

    #
    # Install packages
    #
    Write-Host "Install NIVIDIA GRID driver"
    Install-GridDriver
    Write-Host "Install .NET Framework 3.5"
    Install-WindowsFeature Net-Framework-Core -source \\network\share\sxs

    Write-Host "Install additional packages complete"
}
catch {
    Write-Host "catch: $_"
    $_ | Write-AWSQuickStartException
}