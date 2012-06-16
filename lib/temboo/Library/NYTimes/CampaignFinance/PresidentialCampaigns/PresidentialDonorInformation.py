
###############################################################################
#
# PresidentialDonorInformation
# Retrieve details about individual donors, or a summary of donors from a particular location to a presidential election campaign.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PresidentialDonorInformation(Choreography):

    """
    Create a new instance of the PresidentialDonorInformation Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/CampaignFinance/PresidentialCampaigns/PresidentialDonorInformation')


    def new_input_set(self):
        return PresidentialDonorInformationInputSet()

    def _make_result_set(self, result, path):
        return PresidentialDonorInformationResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PresidentialDonorInformationChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PresidentialDonorInformation
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PresidentialDonorInformationInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NY Times.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the CampaignCycle input for this choreography. ((required, integer) Enter the campaign cycle year in YYYY format.  This must be an even year.)
        """
        def set_CampaignCycle(self, value):
            InputSet._set_input(self, 'CampaignCycle', value)

        """
        Set the value of the FirstName input for this choreography. ((optional, string) Enter the first name of a donor.  This parameter can be used together with LastName and/or Zip)
        """
        def set_FirstName(self, value):
            InputSet._set_input(self, 'FirstName', value)

        """
        Set the value of the LastName input for this choreography. ((optional, string) Enter the last name of an individual donor to be retrieved.)
        """
        def set_LastName(self, value):
            InputSet._set_input(self, 'LastName', value)

        """
        Set the value of the Offset input for this choreography. ((optional, integer) Specify the starting point of the retrieved results, in multiples of 20.  By default, the first 20 results are returned.)
        """
        def set_Offset(self, value):
            InputSet._set_input(self, 'Offset', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Enter json or xml.  Default is json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)

        """
        Set the value of the Zip input for this choreography. ((optional, integer) Enter a zipcode for which donor information wil be retrieved.)
        """
        def set_Zip(self, value):
            InputSet._set_input(self, 'Zip', value)


"""
A ResultSet with methods tailored to the values returned by the PresidentialDonorInformation choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PresidentialDonorInformationResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PresidentialDonorInformationChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PresidentialDonorInformationResultSet(response, path)
