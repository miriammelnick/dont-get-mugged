
###############################################################################
#
# InsertRecords
# Inserts records into your Zoho CRM account.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class InsertRecords(Choreography):

    """
    Create a new instance of the InsertRecords Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Zoho/CRM/InsertRecords')


    def new_input_set(self):
        return InsertRecordsInputSet()

    def _make_result_set(self, result, path):
        return InsertRecordsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return InsertRecordsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the InsertRecords
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class InsertRecordsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by Zoho)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the AnnualRevenue input for this choreography. ((optional, string) Corresponds to the Annual Revenue field in Zoho)
        """
        def set_AnnualRevenue(self, value):
            InputSet._set_input(self, 'AnnualRevenue', value)

        """
        Set the value of the CampaignSource input for this choreography. ((optional, string) Corresponds to the Campaign Source field in Zoho)
        """
        def set_CampaignSource(self, value):
            InputSet._set_input(self, 'CampaignSource', value)

        """
        Set the value of the City input for this choreography. ((optional, string) Corresponds to the City field in Zoho)
        """
        def set_City(self, value):
            InputSet._set_input(self, 'City', value)

        """
        Set the value of the Company input for this choreography. ((optional, string) Corresponds to the Company field in Zoho)
        """
        def set_Company(self, value):
            InputSet._set_input(self, 'Company', value)

        """
        Set the value of the Country input for this choreography. ((optional, string) Corresponds to the Country field in Zoho)
        """
        def set_Country(self, value):
            InputSet._set_input(self, 'Country', value)

        """
        Set the value of the Description input for this choreography. ((optional, string) Corresponds to the Description field in Zoho)
        """
        def set_Description(self, value):
            InputSet._set_input(self, 'Description', value)

        """
        Set the value of the EmailOptOut input for this choreography. ((optional, boolean) Corresponds to the Email Opt Out field in Zoho. Defaults to 0 for false.)
        """
        def set_EmailOptOut(self, value):
            InputSet._set_input(self, 'EmailOptOut', value)

        """
        Set the value of the Email input for this choreography. ((optional, string) Corresponds to the Email field in Zoho)
        """
        def set_Email(self, value):
            InputSet._set_input(self, 'Email', value)

        """
        Set the value of the Fax input for this choreography. ((optional, string) Corresponds to the Fax field in Zoho)
        """
        def set_Fax(self, value):
            InputSet._set_input(self, 'Fax', value)

        """
        Set the value of the FirstName input for this choreography. ((optional, string) Corresponds to the First Name field in Zoho)
        """
        def set_FirstName(self, value):
            InputSet._set_input(self, 'FirstName', value)

        """
        Set the value of the Industry input for this choreography. ((optional, string) Corresponds to the Industry field in Zoho)
        """
        def set_Industry(self, value):
            InputSet._set_input(self, 'Industry', value)

        """
        Set the value of the LastName input for this choreography. ((required, string) Corresponds to the Last Name field in Zoho)
        """
        def set_LastName(self, value):
            InputSet._set_input(self, 'LastName', value)

        """
        Set the value of the LeadOwner input for this choreography. ((optional, string) Corresponds to the Lead Owner field in Zoho)
        """
        def set_LeadOwner(self, value):
            InputSet._set_input(self, 'LeadOwner', value)

        """
        Set the value of the LeadSource input for this choreography. ((optional, string) Corresponds to the Lead Source field in Zoho)
        """
        def set_LeadSource(self, value):
            InputSet._set_input(self, 'LeadSource', value)

        """
        Set the value of the LeadStatus input for this choreography. ((optional, string) Corresponds to the Lead Status field in Zoho)
        """
        def set_LeadStatus(self, value):
            InputSet._set_input(self, 'LeadStatus', value)

        """
        Set the value of the LoginID input for this choreography. ((required, string) Your Zoho username (or login id))
        """
        def set_LoginID(self, value):
            InputSet._set_input(self, 'LoginID', value)

        """
        Set the value of the Mobile input for this choreography. ((optional, string) Corresponds to the Mobile field in Zoho)
        """
        def set_Mobile(self, value):
            InputSet._set_input(self, 'Mobile', value)

        """
        Set the value of the NumOfEmployees input for this choreography. ((optional, string) Corresponds to the Num Of Employees field in Zoho)
        """
        def set_NumOfEmployees(self, value):
            InputSet._set_input(self, 'NumOfEmployees', value)

        """
        Set the value of the Password input for this choreography. ((required, string) Your Zoho password)
        """
        def set_Password(self, value):
            InputSet._set_input(self, 'Password', value)

        """
        Set the value of the Phone input for this choreography. ((optional, string) Corresponds to the Phone field in Zoho)
        """
        def set_Phone(self, value):
            InputSet._set_input(self, 'Phone', value)

        """
        Set the value of the Rating input for this choreography. ((optional, string) Corresponds to the Rating field in Zoho)
        """
        def set_Rating(self, value):
            InputSet._set_input(self, 'Rating', value)

        """
        Set the value of the Salutation input for this choreography. ((optional, string) Corresponds to the Salutation field in Zoho)
        """
        def set_Salutation(self, value):
            InputSet._set_input(self, 'Salutation', value)

        """
        Set the value of the SkypeID input for this choreography. ((optional, string) Corresponds to the Skype ID field in Zoho)
        """
        def set_SkypeID(self, value):
            InputSet._set_input(self, 'SkypeID', value)

        """
        Set the value of the State input for this choreography. ((optional, string) Corresponds to the State field in Zoho)
        """
        def set_State(self, value):
            InputSet._set_input(self, 'State', value)

        """
        Set the value of the Street input for this choreography. ((optional, string) Corresponds to the Street field in Zoho)
        """
        def set_Street(self, value):
            InputSet._set_input(self, 'Street', value)

        """
        Set the value of the Title input for this choreography. ((optional, string) Corresponds to the Title field in Zoho)
        """
        def set_Title(self, value):
            InputSet._set_input(self, 'Title', value)

        """
        Set the value of the Website input for this choreography. ((optional, string) Corresponds to the Website field in Zoho)
        """
        def set_Website(self, value):
            InputSet._set_input(self, 'Website', value)

        """
        Set the value of the ZipCode input for this choreography. ((optional, integer) Corresponds to the Zip Code field in Zoho)
        """
        def set_ZipCode(self, value):
            InputSet._set_input(self, 'ZipCode', value)


"""
A ResultSet with methods tailored to the values returned by the InsertRecords choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class InsertRecordsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((xml) The response from Zoho)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class InsertRecordsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return InsertRecordsResultSet(response, path)
