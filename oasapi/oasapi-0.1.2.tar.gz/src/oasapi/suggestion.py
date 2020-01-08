import ipaddress
import urllib
from enum import Enum

from attr import dataclass

from oasapi.common import find_keys, OPERATIONS_RE, commonprefix
from oasapi.events import Event


def suggestion_health_check(swagger):
    """Return a suggestion to implement an /health check endpoint if it does not exist"""
    suggestions = set()

    for path in swagger["paths"]:
        if "/health" in path:
            # found the health-check
            break
    else:
        suggestions.add(
            Suggestion(
                domain=DomainSuggestion.OPERATION,
                level=1,
                path=("paths",),
                reason=f"you do not have yet an /health endpoint somewhere in your path. It would be great if you could add one "
                       f"(see https://wiki.gem.myengie.com/display/TTA/API+Health for a standard proposal)",
            )
        )

    return suggestions


def suggestion_request_id_log_correlations(swagger):
    """Return a suggestion to implement an /health check endpoint if it does not exist"""
    # retrieve all parameters
    parameters = find_keys(swagger["paths"], "parameters", path=("paths",))

    suggestions = set()

    for params, pth in parameters:
        for param in params:
            if param["name"].lower() == "request-id" and param["in"] == "headers":
                # found the health-check
                break
    else:
        suggestions.add(
            Suggestion(
                domain=DomainSuggestion.OPERATION,
                level=2,
                path=("paths",),
                reason=f"you do not yet require a Request-Id header for your API. "
                f"To improve logging, it would great you implement the Request-Id correlation log "
                f"(see https://wiki.gem.myengie.com/x/DQB6Dw)",
            )
        )

    return suggestions


def suggestion_host_fqdn_https(swagger):
    """Suggest to pass to a FQDN is using IP and to https if using http"""
    suggestions = set()

    schemes = swagger.get("schemes", [])
    if "http" in schemes:
        if "https" in swagger["schemes"]:
            suggestions.add(
                Suggestion(
                    domain=DomainSuggestion.SECURITY,
                    level=1,
                    path=("schemes",),
                    reason=f"you offer access to the API in http (beside https). This is not recommended "
                    f"as traffic can be sniffed/changed during client<->server interactions. "
                    f"You can disable http on your API server",
                )
            )
        else:
            suggestions.add(
                Suggestion(
                    domain=DomainSuggestion.SECURITY,
                    level=1,
                    path=("schemes",),
                    reason=f"you offer access to the API only in http. This is not recommended "
                    f"as traffic can be sniffed/changed during client<->server interactions. "
                    f"You can install SSL certificates on your server to allow https. "
                    f"See https://wiki.gem.myengie.com/x/YgCGDQ for how to request ENGIE signed certificates for internal use.",
                )
            )
    else:
        if not schemes:
            suggestions.add(
                Suggestion(
                    domain=DomainSuggestion.SECURITY,
                    level=1,
                    path=("schemes",),
                    reason=f"No 'schemes' present in the swagger. Ensure you are using https for your API.",
                )
            )

    host = swagger.get("host")
    if host is None:
        suggestions.add(
            Suggestion(
                domain=DomainSuggestion.SECURITY,
                level=1,
                path=("schemes",),
                reason=f"No 'host' present in the swagger. Ensure you are using a FQDN (and not an IP address) for your API server.",
            )
        )
    else:
        hostname = urllib.parse.urlsplit("//" + host).hostname
        try:
            ipaddress.ip_address(hostname)
            suggestions.add(
                Suggestion(
                    domain=DomainSuggestion.SECURITY,
                    level=1,
                    path=("host",),
                    reason=f"you are using an IP address ('{hostname}') instead of a FQDN (fully qualified domain name). "
                    f"This adds a direct dependency against the IP of your API server. "
                    f"To keep flexibility, add a FQDN on *.gem.myengie.com (see https://gemprod.service-now.com/nav_to.do?uri=%2Fcom.glideapp.servicecatalog_cat_item_view.do%3Fv%3D1%26sysparm_id%3D4c772319db3f220092107e400f961971%26sysparm_link_parent%3D09b9e33fdb5fe2006712b34ffe96193d%26sysparm_catalog%3De0d08b13c3330100c8b837659bba8fb4%26sysparm_catalog_view%3Dcatalog_default%26sysparm_view%3Dcatalog_default for the SNOW request).",
                )
            )
        except ValueError:
            pass

    return suggestions


def suggestion_okta_securisation(swagger):
    """Return a suggestion to implement an okta authentication"""
    suggestions = set()

    if "securityDefinitions" not in swagger:
        suggestions.add(
            Suggestion(
                domain=DomainSuggestion.SECURITY,
                level=1,
                path=("securityDefinitions",),
                reason=f"you do not have any security definition to secure your endpoints. "
                f"Please add one or expose your API through the GEMS API Gateway to protect "
                f"it via an API Key or an Okta authentication (contact gemservices@online.engie.com).",
            )
        )

    base_urls = [
        "https://gem-beta.oktapreview.com/oauth2/aus3v6rg3e9zNHMxe0x6/v1",
        "https://gem.okta-emea.com/oauth2/aus1kc58cdNGJB9eb0i7/v1",
    ]

    for sec_name, sec_def in swagger.get("securityDefinitions", {}).items():
        if sec_def["type"] == "oauth2":
            # test implicit flow
            url = sec_def.get("authorizationUrl")
            if url in [f"{base_url}/authorize" for base_url in base_urls]:
                break

            url = sec_def.get("tokenUrl")
            if url in [f"{base_url}/token" for base_url in base_urls]:
                break
    else:
        suggestions.add(
            Suggestion(
                domain=DomainSuggestion.SECURITY,
                level=2,
                path=("securityDefinitions",),
                reason=f"you do not yet use Okta to secure your endpoints. "
                f"Please contact alexandre.giraud@engie.com to move forward on this.",
            )
        )

    return suggestions


def suggestion_security_do_not_return_array(swagger):
    """Return a suggestion to avoid returning JSON response as arrays

    see https://haacked.com/archive/2009/06/25/json-hijacking.aspx/

    It should have been fixed on modern browsers"""
    suggestions = set()

    for path, operations in swagger["paths"].items():
        for verb, details in operations.items():
            if OPERATIONS_RE.match(verb):
                for code, response in details["responses"].items():
                    if not isinstance(response, dict):
                        # it is a reference to a #/responses/
                        continue
                    schema = response.get("schema")
                    if schema:
                        if schema.get("type") == "array":
                            suggestions.add(
                                Suggestion(
                                    domain=DomainSuggestion.DESIGN,
                                    level=1,
                                    path=("paths", path, verb, code, "schema", "type"),
                                    reason=f"your endpoint is returning an array as JSON response, which is vulnerable to JSON hijacking "
                                    f"(see https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/AJAX_Security_Cheat_Sheet.md#protect-against-json-hijacking-for-older-browsers)",
                                )
                            )

    return suggestions


def suggestion_apidesign_length_path(swagger):
    """Return a suggestion to reduce the length of the API path"""
    suggestions = set()

    paths = list(swagger["paths"])
    append_base_path = commonprefix(paths)
    N = len(append_base_path)

    for path in paths:
        L = path[N:].count("/")
        if L > 5:
            suggestions.add(
                Suggestion(
                    domain=DomainSuggestion.DESIGN,
                    level=1,
                    path=("paths", path),
                    reason=f"your API path has {L} levels of depth (not taking into account the common part '{append_base_path}'). "
                    f"Good practice is to avoid more than 5 levels of depth in the path. "
                    f"Consider reviewing your path structure (feel free to contact gemservices@online.engie.com for peer reviewing your swagger).",
                )
            )

    return suggestions


def suggestion_documentation(swagger):  # noqa: C901
    suggestions = set()

    def add_doc_action(path, mode: Mode = Mode.OPERATION):
        obj = swagger
        for i in path:
            obj = obj[i]

        description = obj.get("description")
        summary = obj.get("summary")

        # handle summary
        if summary is None:
            if description is None:
                # nothing at all
                suggestions.add(
                    Suggestion(
                        domain=DomainSuggestion.DOCUMENTATION,
                        level=1,
                        path=tuple(path),
                        reason=f"the {mode.value} does not contain neither a 'summary' nor a 'description' field. Add these to clarify the purpose of your {mode.value}",
                    )
                )
            elif mode != Mode.API:
                # a description but no summary => bad display in swagger-ui
                suggestions.add(
                    Suggestion(
                        domain=DomainSuggestion.DOCUMENTATION,
                        level=1,
                        path=tuple(path),
                        reason=f"the {mode.value} has a 'description' field but no 'summary'. "
                        f"Add the latter as it is often used in Swagger visualisations (swagger-ui, redoc, ...) {mode.value}",
                    )
                )
        else:
            if description is None and False:
                # missing description
                suggestions.add(
                    Suggestion(
                        domain=DomainSuggestion.DOCUMENTATION,
                        level=1,
                        path=tuple(path),
                        reason=f"the {mode.value} does not contain a 'description' field. Check if it is worth to add more documentation in the 'description' field",
                    )
                )
            else:
                # all is there
                pass

        # check length of fields
        if description and len(description) < 20:
            suggestions.add(
                Suggestion(
                    domain=DomainSuggestion.DOCUMENTATION,
                    level=1,
                    path=tuple(path) + ("description",),
                    reason=f"the {mode.value} 'description' field is quite short (less than 20 characters), do not hesitate to be a tad more verbose",
                )
            )
        if summary and len(summary) > 100:
            suggestions.add(
                Suggestion(
                    domain=DomainSuggestion.DOCUMENTATION,
                    level=1,
                    path=tuple(path) + ("summary",),
                    reason=f"the {mode.value} 'summary' field is quite long (more than 100 characters), do not hesitate to move part of if to the 'description' field",
                )
            )

    add_doc_action(["info"], mode=Mode.API)

    for path, operations in swagger["paths"].items():
        for verb, details in operations.items():
            if OPERATIONS_RE.match(verb):
                add_doc_action(["paths", path, verb], mode=Mode.OPERATION)

    return suggestions


class Mode(Enum):
    API = "api"
    OPERATION = "operation"


@dataclass(frozen=True)
class DomainSuggestion(Enum):
    DESIGN = 1
    BUILD = 2
    DOCUMENTATION = 3
    SECURITY = 4
    OPERATION = 5


@dataclass(frozen=True)
class Suggestion(Event):
    domain: DomainSuggestion
    level: int

    @property
    def type(self):
        return f"Suggestion for improved API {self.domain.name.lower().capitalize()} (maturity level {self.level})"
