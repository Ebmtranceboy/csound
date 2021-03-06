{
    "targets":
    [
        {
            "target_name": "csound",
            "sources":
            [
                "jscsound.cpp",
            ],
            'conditions':
            [
                ['OS=="win"',
                    {
                        'libraries':
                        [
                            '-l$(CSOUND_HOME)/csound64.lib',
                        ],
                        'include_dirs':
                        [
                            '$(CSOUND_HOME)/include',
                        ],
                        'configurations':
                        {
                            'Debug':
                            {
                                'msvs_settings':
                                {
                                    'VCCLCompilerTool':
                                    {
                                        'WarningLevel': 4,
                                        'ExceptionHandling': 1,
                                        'DisableSpecificWarnings': [4100, 4127, 4201, 4244, 4267, 4506, 4611, 4714]
                                    }
                                }
                            },
                            'Release':
                            {
                                'msvs_settings':
                                {
                                    'VCCLCompilerTool':
                                    {
                                        'WarningLevel': 4,
                                        'ExceptionHandling': 1,
                                        'DisableSpecificWarnings': [4100, 4127, 4201, 4244, 4267, 4506, 4611, 4714]
                                    }
                                }
                            }
                        },
                    }
                ]
            ]
        }
    ]
}
