
###############################################################################
#
# PresidentialStateZipTotals
# Retrieve the total amount of donations aggregated by a specified location (by state and/or zipcode).
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class PresidentialStateZipTotals(Choreography):

    """
    Create a new instance of the PresidentialStateZipTotals Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/NYTimes/CampaignFinance/PresidentialCampaigns/PresidentialStateZipTotals')


    def new_input_set(self):
        return PresidentialStateZipTotalsInputSet()

    def _make_result_set(self, result, path):
        return PresidentialStateZipTotalsResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return PresidentialStateZipTotalsChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the PresidentialStateZipTotals
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class PresidentialStateZipTotalsInputSet(InputSet):
        """
        Set the value of the APIKey input for this choreography. ((required, string) The API Key provided by NY Times.)
        """
        def set_APIKey(self, value):
            InputSet._set_input(self, 'APIKey', value)

        """
        Set the value of the CampaignCycle input for this choreography. ((required, integer) Enter the campaign cycle year in YYYY format.  This must be an even year. )
        """
        def set_CampaignCycle(self, value):
            InputSet._set_input(self, 'CampaignCycle', value)

        """
        Set the value of the Location input for this choreography. ((required, string) Enter the location for which data will be retrieved. If ResourceType = states, use a two-letter state abbreviation (example: NY).  For zips, enter a five-digit zip code.)
        """
        def set_Location(self, value):
            InputSet._set_input(self, 'Location', value)

        """
        Set the value of the ResourceType input for this choreography. ((required, string) Specify the type of resource to use when retrieving donor data. Valid formats include: zips, or states.)
        """
        def set_ResourceType(self, value):
            InputSet._set_input(self, 'ResourceType', value)

        """
        Set the value of the ResponseFormat input for this choreography. ((optional, string) Enter json or xml.  Default is json.)
        """
        def set_ResponseFormat(self, value):
            InputSet._set_input(self, 'ResponseFormat', value)


"""
A ResultSet with methods tailored to the values returned by the PresidentialStateZipTotals choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class PresidentialStateZipTotalsResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. (The response from the NY Times API corresponds to the setting (json, or xml) entered in the ResponseFormat variable.  Default is set to json.)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class PresidentialStateZipTotalsChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return PresidentialStateZipTotalsResultSet(response, path)
