
###############################################################################
#
# LogWater
# Log a new water entry for a particular date.
#
# Python version 2.6
#
###############################################################################

from temboo.core.choreography import Choreography
from temboo.core.choreography import InputSet
from temboo.core.choreography import ResultSet
from temboo.core.choreography import ChoreographyExecution


class LogWater(Choreography):

    """
    Create a new instance of the LogWater Choreography. A TembooSession object, containing a valid
    set of Temboo credentials, must be supplied.
    """
    def __init__(self, temboo_session):
        Choreography.__init__(self, temboo_session, '/Library/Fitbit/LogWater')


    def new_input_set(self):
        return LogWaterInputSet()

    def _make_result_set(self, result, path):
        return LogWaterResultSet(result, path)

    def _make_execution(self, session, exec_id, path):
        return LogWaterChoreographyExecution(session, exec_id, path)

"""
An InputSet with methods appropriate for specifying the inputs to the LogWater
choreography. The InputSet object is used to specify input parameters when executing this choreo.
"""
class LogWaterInputSet(InputSet):
        """
        Set the value of the Amount input for this choreography. ((decimal) The amount of water consumed. Corresponds to the Unit input.)
        """
        def set_Amount(self, value):
            InputSet._set_input(self, 'Amount', value)

        """
        Set the value of the Date input for this choreography. ((date) The date that corresponds with the new log entry (in the format yyyy-MM-dd))
        """
        def set_Date(self, value):
            InputSet._set_input(self, 'Date', value)

        """
        Set the value of the Format input for this choreography. ((optional, string) The format that you want the response to be in: xml or json. Defaults to xml.)
        """
        def set_Format(self, value):
            InputSet._set_input(self, 'Format', value)

        """
        Set the value of the OauthConsumerKey input for this choreography. ((string) The Oauth Consumer Key provided by Fitbit after registering your application)
        """
        def set_OauthConsumerKey(self, value):
            InputSet._set_input(self, 'OauthConsumerKey', value)

        """
        Set the value of the OauthConsumerSecret input for this choreography. ((string) The Oauth Consumer Secret provided by Fitbit after registering your application)
        """
        def set_OauthConsumerSecret(self, value):
            InputSet._set_input(self, 'OauthConsumerSecret', value)

        """
        Set the value of the OauthTokenSecret input for this choreography. ((string) The Oauth Token Secret retrieved during the Oauth process)
        """
        def set_OauthTokenSecret(self, value):
            InputSet._set_input(self, 'OauthTokenSecret', value)

        """
        Set the value of the OauthToken input for this choreography. ((string) The Oauth Token retrieved during the Oauth process)
        """
        def set_OauthToken(self, value):
            InputSet._set_input(self, 'OauthToken', value)

        """
        Set the value of the Unit input for this choreography. ((string) Unit of measurement for the water entry. Valid values: 'ml', 'fl oz', or 'cup'. )
        """
        def set_Unit(self, value):
            InputSet._set_input(self, 'Unit', value)

        """
        Set the value of the UserId input for this choreography. ((optional, string) The user's encoded id. Defaults to "-" (dash) which will return data for the user associated with the token credentials provided. )
        """
        def set_UserId(self, value):
            InputSet._set_input(self, 'UserId', value)


"""
A ResultSet with methods tailored to the values returned by the LogWater choreography.
The ResultSet object is used to retrieve the results of a choreography execution.
"""
class LogWaterResultSet(ResultSet):
        """
        Retrieve the value for the "Response" output from this choreography execution. ((XML) The response from Fitbit in XML format)
        """
        def get_Response(self):
            return self._output.get('Response', None)

class LogWaterChoreographyExecution(ChoreographyExecution):
    
    def _make_result_set(self, response, path):
        return LogWaterResultSet(response, path)
