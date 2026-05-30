class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = dict()

        for domain in cpdomains:
            cpd = domain.split()
            if cpd[1] not in domains:
                domains[cpd[1]] = int(cpd[0])
            else:
                domains[cpd[1]] += int(cpd[0])
            while(True):
                next_level = cpd[1].split('.', 1)
                if len(next_level) == 1:
                    break
                cpd[1] = next_level[1]
                if cpd[1] not in domains:
                    domains[cpd[1]] = int(cpd[0])
                else:
                    domains[cpd[1]] += int(cpd[0])

        sdv = []

        for k,v in domains.items():
            sdv.append(str(v) + " " + k)

        return sdv

