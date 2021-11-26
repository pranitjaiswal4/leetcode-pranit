class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()
        
        def checkValid(email):
            local, domain = email.split("@")
            
            local = local.split('+')[0].replace('.', '')
            
            valid = local + '@' + domain
            return valid
            
        for email in emails:
            uniqueEmails.add(checkValid(email))
            
        return len(uniqueEmails)
