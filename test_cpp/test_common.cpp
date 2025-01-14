#include <iostream>
#include <unordered_map>

namespace local {
enum Reason : uint64_t {
    SUCCESS = 0,
    UNKNOWN = 1,
    INVALID_PARAM = 2,
    INVALID_REQ = 3,
    INVALID_RESP = 4,
    INVALID_RPC = 5,
};
}

namespace pb {
enum Reason_pb : int {
    SUCCESS = 0,
    UNKNOWN = 1,
    INVALID_PARAM = 12,
    INVALID_REQ = 13,
    INVALID_RESP = 14,
    INVALID_RPC = 15,
};
}

pb::Reason_pb map_reason(int r) {
    switch (r) {
        case local::Reason::SUCCESS:
            return pb::Reason_pb::SUCCESS;
        case local::Reason::UNKNOWN:
            return pb::Reason_pb::UNKNOWN;
        case 2 ... 100:
            return static_cast<pb::Reason_pb>(10 + r);
        default:
            return static_cast<pb::Reason_pb>(100 + r);
    }
}

pb::Reason_pb map_reason(local::Reason r) {
    return map_reason(static_cast<int>(r));
}

#define CASE_STR(x) case x: return #x;

std::string reason_str(pb::Reason_pb r) {
    switch (r) {
        CASE_STR(pb::Reason_pb::SUCCESS);
        CASE_STR(pb::Reason_pb::UNKNOWN);
        CASE_STR(pb::Reason_pb::INVALID_PARAM);
        CASE_STR(pb::Reason_pb::INVALID_REQ);
        CASE_STR(pb::Reason_pb::INVALID_RESP);
        CASE_STR(pb::Reason_pb::INVALID_RPC);
        default:
            return "UNKNOWN";
    }
}

int main() {
    std::unordered_map<int64_t, int64_t> reason_map;
    reason_map[1] = 3;
    reason_map[2] = 4;
    for (const auto& item : reason_map) {
        if (item.first == 1) {
            std::cout << "hit: " << reason_str(map_reason(item.second)) << std::endl;
        } else {
            std::cout << "not hit: " << reason_str(map_reason(item.second)) << std::endl;
        }
    }
    return 0;
}