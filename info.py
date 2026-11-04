"""
payload requires:

@dataclass
class creationRequest(BaseModel):
    name: str
    security: dict
    privacy: dict
    parentalControl: dict
    denylist: list(dict)
    allowlist: list(dict)
    settings: dict
"""

endpoints = {
    "/profiles": {
        "method": ["GET", "POST"],
        "payload": "None",
        "description": "Returns id info with GET & creates a new profile with POST",
    },
    "/profiles/{profile_id}": {
        "method": ["GET", "DELETE"],
        "payload": "None",
        "description": "Returns the complete information of the given profile_id with GET, deletes the profile with DELETE",
    },
    "/privacy/blocklists": {
        "method": ["GET"],
        "payload": "None",
        "description": "Blocklists selected in the privacy tab",
    },
    "/analytics/status": {
        "method": ["GET"],
        "payload": "None",
        "description": "Aggregate of Block, Allowed queries",
    },
    "/analytics/protocols": {
        "method": ["GET"],
        "payload": "None",
        "description": "The protocol being used for DNS resolution, DoH, DoT",
    },
    "/analytics/ips": {
        "method": ["GET"],
        "payload": "None",
        "description": "IPs and the geolocation information of the queries",
    },
    "/analytics/reasons": {
        "method": ["GET"],
        "payload": "None",
        "description": "Blocklists and total queries that they were involved in blocking",
    },
    "/allowlist": {
        "method": ["GET"],
        "payload": "None",
        "description": "Returns information about the domains in the allowlist",
    },
    "/settings": {
        "method": ["GET"],
        "payload": "None",
        "description": "Settings page information i.e information about logging, performance and web3 etc.",
    },
    "/settings/performance": {
        "method": ["GET"],
        "payload": "None",
        "description": "Information about caching, CNAME flattening, and ECS",
    },
    "/denylist": {"method": ["GET", "POST"], "description": ""},
}
