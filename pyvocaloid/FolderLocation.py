
import os

class FolderLocation:
    PathSystemData = os.environ[“CommonProgramFiles”] + "VOCALOID5"
    public static readonly string PathSystemStylePreset = Path.Combine(FolderLocation.PathSystemData, "StylePreset")
    public static readonly string PathSystemMedia = Path.Combine(FolderLocation.PathSystemData, "Media")
    public static readonly string PathSystemMESingingSkill = Path.Combine(FolderLocation.PathSystemData, "MIDIEffect", "SingingSkill")
    public static readonly string PathSystemMERobotVoice = Path.Combine(FolderLocation.PathSystemData, "MIDIEffect", "RobotVoice")
    public static readonly string PathSystemVoicelib = Path.Combine(FolderLocation.PathSystemData, "Voicelib")
    public static readonly string PathSystemAttackReleaselib = Path.Combine(FolderLocation.PathSystemData, "AttackReleaselib")
    public static readonly string PathSystemExplib = Path.Combine(FolderLocation.PathSystemData, "Explib")
    public static readonly string PathSystemRscVoice = Path.Combine(FolderLocation.PathSystemData, "Resource", "Voice")
    public static readonly string PathSystemRscARIcon = Path.Combine(FolderLocation.PathSystemData, "Resource", "AttackRelease", "Icon")
    public static readonly string PathSystemRscARPreview = Path.Combine(FolderLocation.PathSystemData, "Resource", "AttackRelease", "Preview")
    private static readonly string PathUserData = Path.Combine(Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData), "VOCALOID5")
    public static readonly string PathUserStylePreset = Path.Combine(FolderLocation.PathUserData, "StylePreset")
    public static readonly string PathUserMedia = Path.Combine(FolderLocation.PathUserData, "Media")
    public static readonly string PathUserMESingingSkill = Path.Combine(FolderLocation.PathUserData, "MIDIEffect", "SingingSkill")
    public static readonly string PathUserUdic = Path.Combine(FolderLocation.PathUserData, "Udic")
    public static readonly string PathUserShortcut = Path.Combine(FolderLocation.PathUserData, "Shortcut")
    public static readonly string PathUserContentsList = Path.Combine(FolderLocation.PathUserData, "Contents")
    private const string fNameApp = "VOCALOID5"
    private const string fNameStylePreset = "StylePreset"
    private const string fNameMedia = "Media"
    private const string fNameMidiEffect = "MIDIEffect"
    private const string fNameSingingSkill = "SingingSkill"
    private const string fNameRobotVoice = "RobotVoice"
    private const string fNameVoicelib = "Voicelib"
    private const string fNameAttackReleaselib = "AttackReleaselib"
    private const string fNameExplib = "Explib"
    private const string fNameResource = "Resource"
    private const string fNameVoice = "Voice"
    private const string fNameAttackRelease = "AttackRelease"
    private const string fNameIcon = "Icon"
    private const string fNamePreview = "Preview"
    private const string fNameUdic = "Udic"
    private const string fNameShortcut = "Shortcut"
    private const string fNameContentsList = "Contents"