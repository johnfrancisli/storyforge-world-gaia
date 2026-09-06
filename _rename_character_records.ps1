param(
  [switch]$Apply,
  [switch]$RepairAliases
)

$ErrorActionPreference = 'Stop'
$WorkspaceRoot = [System.IO.Path]::GetFullPath($PSScriptRoot)
$CharacterRoot = [System.IO.Path]::GetFullPath((Join-Path $WorkspaceRoot 'records\characters'))

if (-not $CharacterRoot.StartsWith($WorkspaceRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
  throw "Character directory resolved outside the workspace: $CharacterRoot"
}

# Only names that need editorial correction are listed here. Every record ID and
# filename is normalized from its resulting stable display name below.
$NameOverrides = @{
  'character:apprentice-tari' = 'Tari River-Listener'
  'character:chief-lani' = 'Lani Reef-Born'
  'character:chief-oron' = 'Oron Deep-Root'
  'character:daimyo-takeda' = 'Takeda Renji'
  'character:desert-guide-rashid' = 'Rashid al-Rimal'
  'character:djinn-zuhayr' = 'Zuhayr the Patient'
  'character:elder-wayfinder-pua' = 'Pua Star-Memory'
  'character:explorer-dr-voss' = 'Voss Alemann'
  'character:general-lu-fang' = 'Lu Fang'
  'character:hunter-jaguar' = 'Kaa Night-Pelt'
  'character:jarl-sigrid' = 'Sigrid Hallvarsdottir'
  'character:judge-tariq' = 'Tariq al-Mir'
  'character:king-aldran' = 'Aldran Valdris III'
  'character:kuro' = 'Kagemori Kuro'
  'character:merchant-zhou' = 'Zhou Ba'
  'character:miko-sora' = 'Amemiya Sora'
  'character:monk-jian' = 'Jian Yi'
  'character:prince-roderick' = 'Roderick Valdris'
  'character:princess-elara' = 'Elara Valdris'
  'character:shaman-nara' = 'Nara Stillwater'
  'character:shogun-ashikara' = 'Ashikara Yoshito'
  'character:sir-aldrich' = 'Aldrich Whitmore'
  'character:skald-ravn' = 'Ravn Word-Weaver'
  'character:spice-merchant-layla' = 'Layla al-Zaffari'
  'character:strategist-mei' = 'Mei Lin'
  'character:tattoo-artist-mana' = 'Mana Tide-Ink'
  'character:tengu-soji' = 'Soji'
  'character:the-wolf' = 'Garrick Moorcroft'
  'character:tsu-aki-cook' = 'Morita Aki'
  'character:tsu-akira-teacher' = 'Kuroda Akira'
  'character:tsu-baba-storyteller' = 'Matsuda Kiku'
  'character:tsu-chiyo-child' = 'Kobayashi Chiyo'
  'character:tsu-dai-guard-captain' = 'Mori Daichi'
  'character:tsu-emi-weaver' = 'Fujita Emi'
  'character:tsu-fumiko-koto' = 'Hayashi Fumiko'
  'character:tsu-goro-merchant' = 'Ishikawa Goro'
  'character:tsu-hana-messenger' = 'Tachibana Hana'
  'character:tsu-iso-fishwife' = 'Hamada Iso'
  'character:tsu-jinichi-monk' = 'Okabe Jinichi'
  'character:tsu-jiro-elder' = 'Sakurai Jiro'
  'character:tsu-kazue-smith' = 'Shibata Kazue'
  'character:tsu-kenta-child' = 'Arakawa Kenta'
  'character:tsu-kinu-tattoo' = 'Hoshino Kinu'
  'character:tsu-kohana-oiran' = 'Ayase Kohana'
  'character:tsu-machi-merchant' = 'Sugawara Machi'
  'character:tsu-mai-dancer' = 'Fujimoto Mai'
  'character:tsu-mei-maskmaker' = 'Kurosawa Mei'
  'character:tsu-miko-yuki' = 'Shimizu Yuki'
  'character:tsu-nana-herbalist' = 'Aoyama Nana'
  'character:tsu-natsu-farmer' = 'Endo Natsuko'
  'character:tsu-prince-haru' = 'Ashikara Haru'
  'character:tsu-prince-ren' = 'Ashikara Renjiro'
  'character:tsu-rei-guard' = 'Takamori Rei'
  'character:tsu-rin-florist' = 'Hanabusa Rin'
  'character:tsu-rui-gambler' = 'Kanzaki Rui'
  'character:tsu-ryo-lantern' = 'Ando Ryo'
  'character:tsu-satsuki-tea-teacher' = 'Ichinose Satsuki'
  'character:tsu-saya-brewer' = 'Morikawa Saya'
  'character:tsu-shiori-librarian' = 'Minase Shiori'
  'character:tsu-sho-brewer-apprentice' = 'Tanabe Sho'
  'character:tsu-taro-fisherman' = 'Uehara Taro'
  'character:tsu-tomi-servant' = 'Sakaki Tomi'
  'character:tsu-tsubaki-potter' = 'Mashiro Tsubaki'
  'character:tsu-ume-stable' = 'Nomura Ume'
  'character:tsu-yuri-bathhouse' = 'Onodera Yuri'
  'character:val-aldric-stonehand' = 'Aldric Stonehand'
  'character:volva-helga' = 'Helga Rune-Sight'
  'character:cao-shen' = 'Cao Shen'
  'character:warlord-sun-liang' = 'Sun Liang'
  'character:wayfinder-kai' = 'Kai Far-Horizon'
  'character:whale-speaker-fin' = 'Fin Deep-Voice'
  'character:young-jarl-erik' = 'Erik Stone-eye'
  'character:tsu-danuki-tanuki' = 'Danzaburo'
  'character:tsu-goki-oni' = 'Goki'
  'character:tsu-katsura-kitsune' = 'Katsura'
  'character:tsu-kayo-rokurokubi' = 'Kayo'
  'character:tsu-suzu-tengu' = 'Suzume'
  'character:tsu-yukina-spirit' = 'Yukina'
  'character:san-mizuhito-taro' = 'Tao Renshui'
  'character:tide-ariki-lost-chief' = 'Ariki Storm-Shelter'
  'character:tide-tamatoa-chief-son' = 'Tamatoa Wave-Born'
  'character:ver-zel-temple-guard' = 'Zel Stone-Watch'
}

$LegacyIdMap = @{
  'character:jarl-sigrid' = 'character:sigrid-hallvarsdottir'
}

$ExtraAliases = @{
  'character:hra-sigrid-hallvarsdottir' = @('Jarl Sigrid Hallvarsdottir')
}

function ConvertTo-StableSlug([string]$Name) {
  $normalized = $Name.Normalize([Text.NormalizationForm]::FormD)
  $builder = [Text.StringBuilder]::new()
  foreach ($char in $normalized.ToCharArray()) {
    if ([Globalization.CharUnicodeInfo]::GetUnicodeCategory($char) -ne [Globalization.UnicodeCategory]::NonSpacingMark) {
      [void]$builder.Append($char)
    }
  }
  $slug = $builder.ToString().Normalize([Text.NormalizationForm]::FormC).ToLowerInvariant()
  $slug = $slug -replace "['’]", ''
  $slug = $slug -replace '[^a-z0-9]+', '-'
  return $slug.Trim('-')
}

function ConvertTo-YamlSingleQuoted([string]$Value) {
  return "'" + $Value.Replace("'", "''") + "'"
}

if ($RepairAliases) {
  $aliasesByFinalId = @{}
  foreach ($pair in $NameOverrides.GetEnumerator()) {
    $oldId = [string]$pair.Key
    $finalName = [string]$pair.Value
    $finalId = 'character:' + (ConvertTo-StableSlug $finalName)
    $sourcePath = (@(& git grep -l -F "id: $oldId" HEAD -- records/characters 2>$null) | Select-Object -First 1) -replace '^HEAD:', ''
    if (-not $sourcePath) { continue }
    $sourceText = (& git show "HEAD:$sourcePath") -join "`n"
    $oldName = [regex]::Match($sourceText, '(?m)^name: (.+)$').Groups[1].Value.Trim()
    if ($oldName -and $oldName -ne $finalName) {
      if (-not $aliasesByFinalId.ContainsKey($finalId)) { $aliasesByFinalId[$finalId] = @() }
      $aliasesByFinalId[$finalId] += $oldName
    }
  }
  foreach ($oldId in $ExtraAliases.Keys) {
    $sourcePath = (@(& git grep -l -F "id: $oldId" HEAD -- records/characters 2>$null) | Select-Object -First 1) -replace '^HEAD:', ''
    if (-not $sourcePath) { continue }
    $sourceText = (& git show "HEAD:$sourcePath") -join "`n"
    $name = [regex]::Match($sourceText, '(?m)^name: (.+)$').Groups[1].Value.Trim()
    $finalId = 'character:' + (ConvertTo-StableSlug $name)
    if (-not $aliasesByFinalId.ContainsKey($finalId)) { $aliasesByFinalId[$finalId] = @() }
    $aliasesByFinalId[$finalId] += $ExtraAliases[$oldId]
  }

  $updatedCount = 0
  foreach ($finalId in $aliasesByFinalId.Keys) {
    $slug = $finalId.Substring('character:'.Length)
    $file = Join-Path $CharacterRoot "$slug.md"
    if (-not (Test-Path -LiteralPath $file)) { throw "Alias target not found: $file" }
    $content = Get-Content -LiteralPath $file -Raw
    $newline = if ($content.Contains("`r`n")) { "`r`n" } else { "`n" }
    $aliases = @($aliasesByFinalId[$finalId] | Sort-Object -Unique)
    if (-not $aliases.Count) { continue }
    $aliasBlock = 'aliases:' + $newline + (($aliases | ForEach-Object { '- ' + (ConvertTo-YamlSingleQuoted $_) }) -join $newline)
    if ($content -match '(?m)^aliases: \[\]\r?$') {
      $content = [regex]::Replace($content, '(?m)^aliases: \[\]\r?$', $aliasBlock)
      Set-Content -LiteralPath $file -Value $content -Encoding utf8NoBOM -NoNewline
      $updatedCount++
    }
  }
  Write-Output "Restored aliases on $updatedCount character records."
  exit 0
}

$Records = foreach ($file in Get-ChildItem -LiteralPath $CharacterRoot -Filter '*.md' -File) {
  $content = Get-Content -LiteralPath $file.FullName -Raw
  $oldIdMatch = [regex]::Match($content, '(?m)^id: (.+)$')
  $oldNameMatch = [regex]::Match($content, '(?m)^name: (.+)$')
  if (-not $oldIdMatch.Success -or -not $oldNameMatch.Success) {
    throw "Missing id or name in $($file.FullName)"
  }

  $oldId = $oldIdMatch.Groups[1].Value.Trim()
  $oldName = $oldNameMatch.Groups[1].Value.Trim()
  $finalName = if ($NameOverrides.ContainsKey($oldId)) { $NameOverrides[$oldId] } else { $oldName }
  $slug = ConvertTo-StableSlug $finalName
  if ([string]::IsNullOrWhiteSpace($slug)) {
    throw "Could not derive a stable slug for $oldId ($finalName)"
  }

  [pscustomobject]@{
    Source = $file.FullName
    OldFileName = $file.Name
    OldId = $oldId
    OldName = $oldName
    FinalName = $finalName
    FinalId = "character:$slug"
    FinalFileName = "$slug.md"
  }
}

$DuplicateIds = @($Records | Group-Object FinalId | Where-Object Count -gt 1)
$DuplicateFiles = @($Records | Group-Object FinalFileName | Where-Object Count -gt 1)
if ($DuplicateIds.Count -or $DuplicateFiles.Count) {
  $details = @($DuplicateIds.Name + $DuplicateFiles.Name | Sort-Object -Unique) -join ', '
  throw "Final character identities are not unique: $details"
}

$ChangedNames = @($Records | Where-Object { $_.OldName -ne $_.FinalName })
$ChangedIds = @($Records | Where-Object { $_.OldId -ne $_.FinalId })
$ChangedFiles = @($Records | Where-Object { $_.OldFileName -ne $_.FinalFileName })

Write-Output "Character records: $($Records.Count)"
Write-Output "Display names corrected: $($ChangedNames.Count)"
Write-Output "IDs normalized: $($ChangedIds.Count)"
Write-Output "Files to rename: $($ChangedFiles.Count)"

if (-not $Apply) {
  Write-Output 'Dry run only. Re-run with -Apply to perform the migration.'
  exit 0
}

$IdMap = @{}
foreach ($record in $ChangedIds) {
  $IdMap[$record.OldId] = $record.FinalId
}
foreach ($oldId in $LegacyIdMap.Keys) {
  $IdMap[$oldId] = $LegacyIdMap[$oldId]
}

# Update each character record's own identity fields and preserve the former
# display label as an alias whenever the visible name changes.
foreach ($record in $Records) {
  $content = Get-Content -LiteralPath $record.Source -Raw
  $newline = if ($content.Contains("`r`n")) { "`r`n" } else { "`n" }
  $content = [regex]::Replace($content, '(?m)^id: .+$', "id: $($record.FinalId)", 1)
  $content = [regex]::Replace($content, '(?m)^name: .+$', "name: $($record.FinalName)", 1)

  $aliases = @()
  if ($record.OldName -ne $record.FinalName) {
    $aliases += $record.OldName
  }
  if ($ExtraAliases.ContainsKey($record.OldId)) {
    $aliases += $ExtraAliases[$record.OldId]
  }
  $aliases = @($aliases | Sort-Object -Unique)
  if ($aliases.Count) {
    $aliasBlock = 'aliases:' + $newline + (($aliases | ForEach-Object { '- ' + (ConvertTo-YamlSingleQuoted $_) }) -join $newline)
    $content = [regex]::Replace($content, '(?m)^aliases: \[\]$', $aliasBlock, 1)
  }

  Set-Content -LiteralPath $record.Source -Value $content -Encoding utf8NoBOM -NoNewline
}

# Replace every old character ID in all authored Markdown/JSON, including prose
# references inside gm_notes, relationships, and threads.
$TextFiles = Get-ChildItem -LiteralPath $WorkspaceRoot -Recurse -File | Where-Object {
  $_.FullName -notmatch '[\\/]\.git[\\/]' -and $_.Extension -in @('.md', '.json')
}
$IdPairs = @($IdMap.GetEnumerator() | Sort-Object { $_.Key.Length } -Descending)
foreach ($file in $TextFiles) {
  $content = Get-Content -LiteralPath $file.FullName -Raw
  $updated = $content
  foreach ($pair in $IdPairs) {
    $updated = $updated.Replace([string]$pair.Key, [string]$pair.Value)
  }
  if ($updated -cne $content) {
    Set-Content -LiteralPath $file.FullName -Value $updated -Encoding utf8NoBOM -NoNewline
  }
}

# Relationship display labels sometimes contain the old title-bearing display
# name. Keep those labels readable without rewriting ordinary prose references.
$RelationshipRoot = Join-Path $WorkspaceRoot 'records\relationships'
$NamePairs = @($ChangedNames | Where-Object { $_.OldName -match '\s' } | Sort-Object { $_.OldName.Length } -Descending)
foreach ($file in Get-ChildItem -LiteralPath $RelationshipRoot -Filter '*.md' -File) {
  $content = Get-Content -LiteralPath $file.FullName -Raw
  $nameMatch = [regex]::Match($content, '(?m)^name: (.+)$')
  if (-not $nameMatch.Success) { continue }
  $label = $nameMatch.Groups[1].Value
  $updatedLabel = $label
  foreach ($pair in $NamePairs) {
    $updatedLabel = $updatedLabel.Replace($pair.OldName, $pair.FinalName)
  }
  $updatedLabel = $updatedLabel.Replace('Jarl Sigrid Hallvarsdottir', 'Sigrid Hallvarsdottir')
  if ($updatedLabel -cne $label) {
    $content = [regex]::Replace($content, '(?m)^name: .+$', "name: $updatedLabel", 1)
    Set-Content -LiteralPath $file.FullName -Value $content -Encoding utf8NoBOM -NoNewline
  }
}

# Rename in two phases so an existing source filename can safely become another
# record's target without overwrite. All resolved paths are checked first.
$Moves = foreach ($record in $ChangedFiles) {
  $source = [System.IO.Path]::GetFullPath($record.Source)
  $target = [System.IO.Path]::GetFullPath((Join-Path $CharacterRoot $record.FinalFileName))
  if (-not $source.StartsWith($CharacterRoot, [System.StringComparison]::OrdinalIgnoreCase) -or
      -not $target.StartsWith($CharacterRoot, [System.StringComparison]::OrdinalIgnoreCase)) {
    throw "Refusing a character move outside records/characters: $source -> $target"
  }
  [pscustomobject]@{
    Source = $source
    Temporary = Join-Path $CharacterRoot ('.codex-rename-' + [guid]::NewGuid().ToString('N') + '.tmp')
    Target = $target
  }
}

foreach ($move in $Moves) {
  Move-Item -LiteralPath $move.Source -Destination $move.Temporary
}
foreach ($move in $Moves) {
  if (Test-Path -LiteralPath $move.Target) {
    throw "Refusing to overwrite existing target: $($move.Target)"
  }
  Move-Item -LiteralPath $move.Temporary -Destination $move.Target
}

Write-Output 'Character identity migration complete.'
