from dataclasses import dataclass, field
from enum import Enum
import uuid
import websockets

class OutcropEvents(Enum):
    AdditionalContentLoaded, AgentCommand, AgentCreated, ApiInit, AppPaused, AppResumed, AppSuspended, AwardAchievement, BlockBroken, BlockPlaced, BoardTextUpdated, BossKilled, CameraUsed, CauldronUsed, ChunkChanged, ChunkLoaded, ChunkUnloaded, ConfigurationChanged, ConnectionFailed, CraftingSessionCompleted, EndOfDay, EntitySpawned, FileTransmissionCancelled, FileTransmissionCompleted, FileTransmissionStarted, FirstTimeClientOpen, FocusGained, FocusLost, GameSessionComplete, GameSessionStart, HardwareInfo, HasNewContent, ItemAcquired, ItemCrafted, ItemDestroyed, ItemDropped, ItemEnchanted, ItemSmelted, ItemUsed, JoinCanceled, JukeboxUsed, LicenseCensus, MascotCreated, MenuShown, MobInteracted, MobKilled, MultiplayerConnectionStateChanged, MultiplayerRoundEnd, MultiplayerRoundStart, NpcPropertiesUpdated, OptionsUpdated, performanceMetrics, PackImportStage, PlayerBounced, PlayerDied, PlayerJoin, PlayerLeave, PlayerMessage, PlayerTeleported, PlayerTransform, PlayerTravelled, PortalBuilt, PortalUsed, PortfolioExported, PotionBrewed, PurchaseAttempt, PurchaseResolved, RegionalPopup, RespondedToAcceptContent, ScreenChanged, ScreenHeartbeat, SignInToEdu, SignInToXboxLive, SignOutOfXboxLive, SpecialMobBuilt, StartClient, StartWorld, TextToSpeechToggled, UgcDownloadCompleted, UgcDownloadStarted, UploadSkin, VehicleExited, WorldExported, WorldFilesListed, WorldGenerated, WorldLoaded, WorldUnloaded = range(87)


@dataclass
class OutcropHeader:
    version: int = 1
    requestId: str = str(uuid.uuid4())
    messageType: str = 'commandRequest'
    messagePurpose: str = 'subscribe'



@dataclass
class OutcropBody:
    eventName: str = 'PlayerMessage'
    def __post_init__(self):
        for prop, _ in self.__dataclass_fields__.items():
            prop = getattr(self, prop)
            if prop in OutcropEvents.__members__:
                pass
            else:
                raise NameError


@dataclass
class OutcropEvent:
    header: OutcropHeader = field(default_factory=OutcropHeader)
    body: OutcropBody = field(default_factory=OutcropBody)
    _to_dict: set = field(repr=False,default_factory=set)
    def to_dict(self):
        self._to_dict = {}
        self.header_to_dict = dict()
        self.body_to_dict = dict()
        self.header_to_dict["header"] = self.header.__dict__
        self.body_to_dict["body"] = self.body.__dict__
    
        self._to_dict.update(self.header_to_dict)
        self._to_dict.update(self.body_to_dict)
        return self._to_dict
    def to_json(self):
        import json
        return json.dumps(self.to_dict())

class OutcropAPI:
    def __init__(self, customHandler: None = None):
        self.customHandler = customHandler
        self.queueEvent = []
        self.cache = []
    
    def subscribe(self, eventReq: OutcropEvent):
        self.queueEvent.append(eventReq.to_json())
    
    async def handle(self, websocket, path):
        import json

        for eventReq in self.queueEvent:
            await websocket.send(eventReq)

        try:
            async for msg in websocket:
                msg = json.loads(msg)

                self.customHandler(msg)
        except websockets.exceptions.ConnectionClosedError as err:
            print(f"Disconnected:[{err}]")